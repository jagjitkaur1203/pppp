from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()],render_kw={"placeholder": "abc@gmail.com"})
    contact=StringField('Contact',
                        validators=[DataRequired(), Length(min=10, max=10)])
    '''date_of_birth = DateField('Your Date of Birth', 
                        validators=[DataRequired()],render_kw={"placeholder": "YYYY-MM-DD"})
    gender = SelectField('Gender',
                        validators=[DataRequired()],choices=[('Male', 'Male'), ('Female', 'Female'),('Other','Other')])'''
    password = PasswordField('Password',
                        validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class StaffLoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

from wtforms.validators import InputRequired
class CommentForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')
