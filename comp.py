from flask import Flask,flash,redirect,url_for,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL

from os import environ, path
import pymysql 
import math
pymysql.install_as_MySQLdb()
import webbrowser
import draftable
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField,SelectField,RadioField,SelectField
from difflib import SequenceMatcher, Differ
import difflib

app = Flask(__name__,template_folder='demo/template',static_folder="demo/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/pythonproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='5dea345b323975ede673fdc3f87c24e4'
db = SQLAlchemy(app)

class RegForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    contact=StringField('Contact',
                        validators=[DataRequired(), Length(min=10, max=10)])
    option = SelectField('What You Did Before',[DataRequired()],choices=[
            ('pgdca', 'PGDCA'),
            ('Diploma in Computer Science Engineering', 'Diploma in Computer Science Engineering'),
            ('Diploma in Civil Engineering', 'Diploma in Civil Engineering'),
            ('Diploma in Mechanical  Engineering', 'Diploma in Mechanical  Engineering'),
            ('Diploma in Chemical  Engineering', 'Diploma in Chemical  Engineering'),
            ])
    option1 = SelectField('Under Which University',[DataRequired()],choices=[
            ('punjabi university, patiala', 'Punjabi University Patiala'),
            ('punjab university, chandigarh', 'Punjab University Chandigarh'),
            ('Punjab Technical University, Kapurthala', 'Punjab Technical University Kapurthala'),
            ('Chandigarh University, Chandigarh', 'Chandigarh University Chandigarh')])
    appliedfor = SelectField('Applied For',[DataRequired()],choices=[
            ("B.Tech (Computer Science & Engineering)", 'B.Tech (Computer Science & Engineering)'),
            ('B.Tech (Civil Engineering)', 'B.Tech (Civil Engineering)'),
            ('B.Tech (Mechanical  Engineering)', 'B.Tech (Mechanical  Engineering)'),
            ('B.Tech (Chemical  Engineering)', 'B.Tech (Chemical  Engineering)'),
            ('Masters Of Computer Application', 'Masters Of Computer Application'),
            ('M.SC. (Computer Science)', 'M.SC. (Computer Science)')
            ])
    submit = SubmitField('Submit')

class regform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    contact = db.Column(db.String(80),nullable=False)
    qualification = db.Column(db.String(120), nullable=False)
    university=db.Column(db.String(120), nullable=False)
    appliedfor=db.Column(db.String(120), nullable=False)
        

@app.route('/regform1',methods=['GET','POST'])
def regform1():
    form = RegForm() 
    if (form.validate_on_submit) and (request.method == 'POST'):
         email=request.form.get('email')
         contact=request.form.get('contact')
         qualification=request.form.get('option')
         university=request.form.get('option1')
         appliedfor=request.form.get('appliedfor')

         entry= regform(email=email,contact=contact,qualification=qualification,university=university,appliedfor=appliedfor)
         db.session.add(entry)
         db.session.commit()
         flash('Registered Successfully', 'success')
         return redirect(url_for('eligibility'))
    return render_template('regform.html',title='register',form=form)

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/about') 
def about():
    return render_template('about.html',title='About')

@app.route('/handbooks') 
def handbooks():
    return render_template('handbooks.html',title='handbooks')

class AdmissionForm(FlaskForm):
    firstname = StringField('firstname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('lastname',
                        validators=[DataRequired(), Email()],render_kw={"placeholder": "abc@gmail.com"})
    dateofbirth=DateField('dateofbirth',
                        validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField('submit')


class admissionrecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    dateofbirth = db.Column(db.String(120), nullable=False)

@app.route('/admission',methods=['GET','POST']) 
def admission():
    form=AdmissionForm
    if (form.validate_on_submit) and (request.method == 'POST'):
         firstname=request.form.get('firstname')
         lastname=request.form.get('lastname')
         dateofbirth=request.form.get('dateofbirth')
         return redirect(url_for('eligibility'))
    return render_template('admission.html',title='admission',form=form)

class ComparisionForm(FlaskForm):
    file1 = StringField('file1',
                           validators=[DataRequired()])
    file2 = StringField('file2',
                        validators=[DataRequired()])
    submit = SubmitField('submit')

@app.route('/eligibility',methods=['GET','POST']) 
def eligibility():
    form=ComparisionForm
    if (form.validate_on_submit) and (request.method == 'POST'):
        file1=request.form.get('file1')
        file2=request.form.get('file2')
        client = draftable.Client("ENrWsb-test", "df941a9dbdfb9c328caccc3f81892a5b")
        comparisons = client.comparisons
        comparison = comparisons.create('C:/Users/Lenovo/Desktop/demo/PTU_BTech.pdf','C:/Users/Lenovo/Desktop/demo/PU_BTech.pdf')
        url = client.comparisons.signed_viewer_url(comparison.identifier)
        print(url)
        with open('C:/Users/Lenovo/Desktop/demo/pdf1.txt.docx', errors='ignore') as file1, open('C:/Users/Lenovo/Desktop/demo/pdf2.docx',errors='ignore') as file2:
            file_1_data=file1.read()
            file_2_data=file2.read()
            Similarity = SequenceMatcher(None, file_1_data, file_2_data).ratio()
            print(Similarity*100)
            ratio=Similarity*100
            if(ratio>40):
                flash(f"Percentage Ratio= {math.floor(ratio)}. You are eligible, For Further Process and for changes in your form Enquire to Academic Session.",'success')
            else:
                flash(f"Percentage Ratio= {math.floor(ratio)}. You are eligible with bridge courses, For Further Process and for changes in your form  Enquire to Academic Session.",'success')
            # flash(f"You are eligible " if {ratio>60.0} else "You are eligible with bridge courses",'success')
            #flash(f"Percentile ratio=,{ratio}", 'success')
        return redirect(url_for('home'))
    return render_template('eligibility.html',title='eligibility',form=form)


import pymysql
m1 = pymysql.connect(host='localhost',
                             user='root',
                             password='password',                             
                             db='pythonproject',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/database',methods=['GET']) 
def database():
            cur = m1.cursor() 
            cur.execute("""SELECT * FROM commentpost""")
            data = cur.fetchall()
            return render_template('database.html',value=data,title='database')

class RegistrationForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()],render_kw={"placeholder": "abc@gmail.com"})
    contact=StringField('Contact',
                        validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('Password',
                        validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class studentregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/register',methods=['GET','POST']) 
def register():
    form = RegistrationForm() 
    if (form.validate_on_submit) and (request.method == 'POST'):
         username=request.form.get('username')
         email=request.form.get('email')
         contact=request.form.get('contact')
         password=request.form.get('password')
         Studentregister = studentregister.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
         if Studentregister:
             # if a user is found, we want to redirect back to signup page so user can try again
             flash(f'Hi, {form.username.data}!, User Already exists, Login here', 'success')
             return redirect(url_for('login'))
         entry= studentregister(username=username,email=email,contact=contact,password=password)
         db.session.add(entry)
         db.session.commit()
         flash(f'Hi, {form.username.data}!, Login Yourself', 'success')
         return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

@app.route('/login',methods=['GET','POST']) 
def login():
    
    form = LoginForm() 
    if form.validate_on_submit():
        email=request.form.get('email')
        password=request.form.get('password')
        if form.email.data == 'admin@blog.com' and form.password.data == '555555':
            flash('You have been logged in!', 'success')
            return redirect(url_for('regform1'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)


class StaffLoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    

@app.route('/stafflogin',methods=['GET','POST']) 
def stafflogin():
    form = StaffLoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('database'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('stafflogin.html',title='Login',form=form)


class CommentForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

class commentpost(db.Model):
    id = db.Column(db.Integer,unique=True,primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(120), nullable=False)
    
@app.route('/comment',methods=['GET','POST'])
def comment():
    form = CommentForm()
    if (form.validate_on_submit) and (request.method == 'POST'):
        email=request.form.get('email')
        body=request.form.get('body')

        entry= commentpost(email=email,body=body)
        db.session.add(entry)
        db.session.commit()

        flash(f'We will revert back soon,{email}', 'success')
        return redirect(url_for('comment'))
    return render_template('comment.html',title='query',form=form)

if __name__ == '__main__':
    app.run(debug = True) 