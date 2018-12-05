from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email: ', validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
