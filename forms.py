from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import User


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email: ', validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])

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
    title = StringField('Subject: ', validators=[InputRequired()])
    '''room_opts = QuerySelectField(query_factory= , allow_blank=True )'''
