from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired, Email, Length, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from models import User
from wtforms.fields.html5 import DateField, TimeField


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
            raise ValidationError('Username already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email: ', validators=[InputRequired(), Email(), Length(max=50)])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
             raise ValidationError('Email already taken')


class NewPostForm(FlaskForm):
    #title = StringField('Subject: ', validators=[InputRequired()])
    dt = DateField('Date', format='%Y-%m-%d')
    begin = TimeField('Start', format='%h-%m')
    end = TimeField('End', format='%h-%m')
    subject = StringField('Subject', validators= [InputRequired()])
    sub = SelectField(u'Subject', choices=[('1', 'Course 1'), ('2', 'Course 2'), ('3', 'Course 3')])

    #'''room_opts = QuerySelectField(query_factory= , allow_blank=True )'''
