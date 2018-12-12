from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import User, Course


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


def course_query(level):
    return Course.query.filter_by(level=level)


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=4, max=15)])
    level = SelectField('Level: ', validators=[InputRequired()], choices = [('Triennale','trie'), ('Magistrale','magister')])
    #'''course = QuerySelectField('Course: ', query_factory=course_query(level))'''
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


def level_query():
    return Course.query.distinct(Course.level).order_by(Course.level)


'''class NewPostForm(FlaskForm):'''

