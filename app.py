from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import log_reg
import pandas as pd


# App and database creation
app = Flask(__name__)
app.secret_key = "2791Gaston$"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Define database table
class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    mbti = Column(String(40))
    scale_e = Column(Integer)
    scale_n = Column(Integer)
    scale_t = Column(Integer)
    scale_j = Column(Integer)


# Helps with maintaining the user session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# WTForm for Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])


# WTForm for Sign Up
class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=40)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Types page
@app.route("/types")
def types():
    return render_template("types.html")


# Quiz page, login required
@app.route("/quiz", methods=['POST', 'GET'])
@login_required
def quiz():
    if request.method == "POST":

        # Get all answers
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')
        q6 = request.form.get('q6')
        q7 = request.form.get('q7')
        q8 = request.form.get('q8')
        q9 = request.form.get('q9')
        q10 = request.form.get('q10')
        q11 = request.form.get('q11')
        q12 = request.form.get('q12')
        q13 = request.form.get('q13')
        q14 = request.form.get('q14')
        q15 = request.form.get('q15')
        q16 = request.form.get('q16')
        q17 = request.form.get('q17')
        q18 = request.form.get('q18')
        q19 = request.form.get('q19')
        q20 = request.form.get('q20')
        q21 = request.form.get('q21')
        q22 = request.form.get('q22')
        q23 = request.form.get('q23')
        q24 = request.form.get('q24')
        q25 = request.form.get('q25')
        q26 = request.form.get('q26')
        q27 = request.form.get('q27')
        q28 = request.form.get('q28')
        q29 = request.form.get('q29')
        q30 = request.form.get('q30')
        q31 = request.form.get('q31')
        q32 = request.form.get('q32')
        q33 = request.form.get('q33')
        q34 = request.form.get('q34')
        q35 = request.form.get('q35')
        q36 = request.form.get('q36')
        q37 = request.form.get('q37')
        q38 = request.form.get('q38')
        q39 = request.form.get('q39')
        q40 = request.form.get('q40')
        q41 = request.form.get('q41')
        q42 = request.form.get('q42')
        q43 = request.form.get('q43')
        q44 = request.form.get('q44')
        q45 = request.form.get('q45')
        q46 = request.form.get('q46')
        q47 = request.form.get('q47')
        q48 = request.form.get('q48')
        q49 = request.form.get('q49')
        q50 = request.form.get('q50')
        q51 = request.form.get('q51')
        q52 = request.form.get('q52')
        q53 = request.form.get('q53')
        q54 = request.form.get('q54')
        q55 = request.form.get('q55')
        q56 = request.form.get('q56')
        q57 = request.form.get('q57')
        q58 = request.form.get('q58')
        q59 = request.form.get('q59')
        q60 = request.form.get('q60')
        q61 = request.form.get('q61')
        q62 = request.form.get('q62')
        q63 = request.form.get('q63')
        q64 = request.form.get('q64')
        q65 = request.form.get('q65')
        q66 = request.form.get('q66')
        q67 = request.form.get('q67')
        q68 = request.form.get('q68')
        q69 = request.form.get('q69')
        q70 = request.form.get('q70')
        q71 = request.form.get('q71')
        q72 = request.form.get('q72')
        q73 = request.form.get('q73')
        q74 = request.form.get('q74')
        q75 = request.form.get('q75')
        q76 = request.form.get('q76')
        q77 = request.form.get('q77')
        q78 = request.form.get('q78')
        q79 = request.form.get('q79')
        q80 = request.form.get('q80')
        q81 = request.form.get('q81')
        q82 = request.form.get('q82')
        q83 = request.form.get('q83')
        q84 = request.form.get('q84')
        q85 = request.form.get('q85')
        q86 = request.form.get('q86')
        q87 = request.form.get('q87')
        q88 = request.form.get('q88')
        q89 = request.form.get('q89')
        q90 = request.form.get('q90')
        q91 = request.form.get('q91')
        q92 = request.form.get('q92')
        q93 = request.form.get('q93')
        q94 = request.form.get('q94')
        q95 = request.form.get('q95')
        q96 = request.form.get('q96')
        q97 = request.form.get('q97')
        q98 = request.form.get('q98')
        q99 = request.form.get('q99')
        q100 = request.form.get('q100')
        q101 = request.form.get('q101')
        q102 = request.form.get('q102')
        q103 = request.form.get('q103')
        q104 = request.form.get('q104')
        q105 = request.form.get('q105')
        q106 = request.form.get('q106')
        q107 = request.form.get('q107')
        q108 = request.form.get('q108')
        q109 = request.form.get('q109')
        q110 = request.form.get('q110')
        q111 = request.form.get('q111')
        q112 = request.form.get('q112')
        q113 = request.form.get('q113')
        q114 = request.form.get('q114')
        q115 = request.form.get('q115')
        q116 = request.form.get('q116')
        q117 = request.form.get('q117')
        q118 = request.form.get('q118')
        q119 = request.form.get('q119')
        q120 = request.form.get('q120')
        q121 = request.form.get('q121')
        q122 = request.form.get('q122')
        q123 = request.form.get('q123')
        q124 = request.form.get('q124')
        q125 = request.form.get('q125')
        q126 = request.form.get('q126')
        q127 = request.form.get('q127')
        q128 = request.form.get('q128')
        q129 = request.form.get('q129')
        q130 = request.form.get('q130')
        q131 = request.form.get('q131')
        q132 = request.form.get('q132')
        q133 = request.form.get('q133')
        q134 = request.form.get('q134')
        q135 = request.form.get('q135')
        q136 = request.form.get('q136')
        q137 = request.form.get('q137')
        q138 = request.form.get('q138')
        q139 = request.form.get('q139')
        q140 = request.form.get('q140')
        q141 = request.form.get('q141')
        q142 = request.form.get('q142')

        # Convert answers to a list
        answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18,
                   q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34,
                   q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50,
                   q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, q66,
                   q67, q68, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82,
                   q83, q84, q85, q86, q87, q88, q89, q90, q91, q92, q93, q94, q95, q96, q97, q98,
                   q99, q100, q101, q102, q103, q104, q105, q106, q107, q108, q109, q110, q111, q112,
                   q113, q114, q115, q116, q117, q118, q119, q120, q121, q122, q123, q124, q125, q126,
                   q127, q128, q129, q130, q131, q132, q133, q134, q135, q136, q137, q138, q139, q140,
                   q141, q142]

        # Get the number of occurrences of each letter
        scale_e = answers.count("e")
        scale_i = answers.count("i")
        scale_n = answers.count("n")
        scale_s = answers.count("s")
        scale_t = answers.count("t")
        scale_f = answers.count("f")
        scale_j = answers.count("j")
        scale_p = answers.count("p")

        # Construct MBTI
        if scale_e > scale_i:
            ei = "E"
        elif scale_e == scale_i:
            ei = "E"
        else:
            ei = "I"

        if scale_n > scale_s:
            ns = "N"
        elif scale_n == scale_s:
            ns = "N"
        else:
            ns = "S"

        if scale_t > scale_f:
            tf = "T"
        elif scale_t == scale_f:
            tf = "T"
        else:
            tf = "F"

        if scale_j > scale_p:
            jp = "J"
        elif scale_j == scale_p:
            jp = "J"
        else:
            jp = "P"

        calc_mbti = ei + ns + tf + jp

        # Check to make sure calculations are correct in the console
        print(calc_mbti, "E: ", scale_e, "I: ", scale_i, "S: ", scale_s, "N: ", scale_n, "T: ", scale_t, "F: ",
              scale_f, "J: ", scale_j, "P: ", scale_p)

        # Update the database
        user = User.query.filter_by(id=current_user.id).first()
        user.mbti = calc_mbti
        user.scale_e = scale_e
        user.scale_n = scale_n
        user.scale_t = scale_t
        user.scale_j = scale_j
        db.session.commit()

        # Take the user to their results
        return redirect(url_for("results"))

    else:
        return render_template("quiz.html", name=current_user.name)


# Results page, login required
@app.route("/results")
def results():
    user = User.query.filter_by(id=current_user.id).first()
    mbti = user.mbti

    jobs = log_reg.get_job_predictions(user.scale_e, user.scale_n, user.scale_t, user.scale_j)
    hyperlink = "https://www.16personalities.com/" + mbti + "-personality"
    return render_template("results.html", mbti=mbti, jobs=jobs, hyperlink=hyperlink)


# Sign Up page
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    # Initialize form
    form = SignUpForm()

    if form.validate_on_submit():
        # Password security
        hashed_password = generate_password_hash(form.password.data, method="sha256")

        # Check if user already exists in the database
        user_already_exists = User.query.filter_by(email=form.email.data).first()
        if user_already_exists:
            flash("You already have an account with that email address!")
            return redirect(url_for("login"))

        # Create a new user, then go to Login page
        else:
            new_user = User(name=form.name.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("signup.html", form=form)


# Login page
@app.route("/login", methods=['POST', 'GET'])
def login():
    # Initialize form
    form = LoginForm()

    if form.validate_on_submit():

        # Check to see if email exists in the database
        email_exists = User.query.filter_by(email=form.email.data).first()
        if email_exists:

            # Check to see if the password matches for that email
            if check_password_hash(email_exists.password, form.password.data):
                login_user(email_exists)
                flash("Login successful!")

                # If the user's MBTI already exists, take them to results page
                if email_exists.mbti:
                    return redirect(url_for("results"))

                # User has not already taken quiz and needs to take it
                else:
                    return redirect(url_for("quiz"))
            else:
                flash("Incorrect password")
                redirect(url_for("login"))
        else:
            flash("You do not have account yet. Please sign up.")
            return redirect(url_for("signup"))

    return render_template('login.html', form=form)


# View page. Helps with seeing the database entries
@app.route("/view")
def view():
    return render_template("view.html", database=User.query.all())


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
