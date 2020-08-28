import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

######## HOW THIS WORKS ########
## INTRO
# We want to find out how a person's specific personality affects their satisfaction at different jobs they
# might have. Instead of using the computed MBTI psychotype, like ISTP, we are using scales of each MBTI.

## HOW MBTIs WORK
# There are 8 MBTIs. E, I, S, N, T, F, J, P.
# You can either be     E or I,     S or N,     T or F,     J or P
# This creates 16 unique combinations. Examples: ENTP, ESTJ, INTP, ISFJ
# Each person takes the personality quiz. Every question is categorized by either E/I, S/N, T/F, J/P
# There are 35 E/I questions, 37 S/N questions, 35 T/F questions, and 35 J/P questions.
# From these categories, the person's scale_e, scale_n, scale_t, and scale_j are saved.
# scale_i, scale_s, scale_f, and scale_p are not needed because they are inverses of scale_e, scale_n, scale_t,
# and scale_j, respectively.

## OBJECTIVE
# We want to know how a person's personality scales (scale_e, scale_n, scale_t, scale_j) affects their
# predicted satisfaction at 47 different jobs.

## HOW
# First, a logistic regression needs to be performed on the original dataset.
# Read in the data. It contains 11,115 records. Each record has a jobtitle, scale_e, scale_n, scale_t, scale_j, and
# satisfied (1 or 0)


df = pd.read_csv('static/logistic_regression_data.csv')


# The target variable (y) is the satisfaction. It is located at column index 5.
y = df.iloc[:, 5].values


# Dummy variables for jobtitle are needed since it is a categorical variable. 47 different jobs.
jobtitles = pd.get_dummies(df['jobtitle'], drop_first=True)


# Adjust the dataset to prepare for analysis. Drop the columns that are not used.
X = df.drop(columns=['jobtitle', 'satisfied'])


# Add the columns back with the dummy variables
X = pd.concat([X, jobtitles], axis=1)


# Fit the model
logmodel = LogisticRegression(max_iter=1000)
logmodel.fit(X, y)
logmodel.score(X, y)
y_pred = logmodel.predict(X)


# Print this to the console for a report of the model
print(classification_report(y, y_pred))


########################################################################################################################
######## PUTTING NEW DATA THROUGH THE MODEL ########


# Getting all jobtitles, then making dummy variables for those jobs.
jobs = df.jobtitle.unique()
job_list = []
for i in jobs:
    job_list.append(i)
jobs_df = pd.DataFrame(job_list,columns=['jobtitle'])
new_dummy_jobs = pd.get_dummies(jobs_df['jobtitle'],drop_first=True)


# Get scaled satisfaction.
# This was computed by: (total number of people working each job) / (total number of satisfied people at each job)
scales = pd.read_csv('static/scaled_satisfaction.csv')


# Given that a new person already took the quiz and has their scales e, n, t, and j saved in the database,
# run those scales through this function
def get_job_predictions(e, n, t, j):
    new_X = pd.DataFrame({'scale_e': e, 'scale_n': n, 'scale_t': t, 'scale_j': j}, index=range(43))
    new_X = pd.concat([new_X, new_dummy_jobs], axis=1)

    probability = logmodel.predict_proba(new_X)[:, 1]
    results = []

    for i in range(len(new_X)):
        results.append(probability[i])

    results_df = pd.DataFrame(results, columns=['prob'])
    results_df = pd.concat([results_df, jobs_df], axis=1)
    pred = results_df.sort_values(by='jobtitle')
    pred = pred.set_index('jobtitle').join(scales.set_index('jobtitle'))
    pred['compared_to_average'] = pred['prob'] / pred['percent_satisfied']
    pred = pred.round(2)
    results = pred.sort_values(['compared_to_average', 'percent_satisfied'], ascending=(False, False))
    results = results.rename(columns={'jobtitle': "Job",
                                      'prob': "Probability_you_will_be_Satisfied",
                                      'percent_satisfied': "Average_Satisfaction_for_this_Job",
                                      'compared_to_average': "Your_Satisfaction_compared_to_the_Average"})

    return results
