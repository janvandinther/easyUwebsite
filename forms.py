from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from database import User

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email: ', validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Take another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken. Take another one')

