from flask import flash
from flask_login import login_user
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length, Email

from database.controller import UsersRepository

users_repository = UsersRepository()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')

    def validate_username(self, username):
        __user = users_repository.get_user(payload={'username': username.data})
        if __user is None or not __user.check_password(self.password.data):
            flash(f'Invalid username or password')
            raise ValidationError()
        login_user(__user, remember=self.remember.data)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        __user = users_repository.get_user(payload={'username': username.data})
        if __user is not None:
            raise ValidationError('The given username is taken. Use another')

    def validate_email(self, email):
        __user = users_repository.get_user(payload={'email': email.data})
        if __user is not None:
            raise ValidationError('The given E-Mail is taken. Use another')


# todo create RecoveryForm
class RecoveryForm(FlaskForm):
    username = StringField('Username')
    email = StringField('E-mail', validators=[Email()])
    submit = SubmitField('Restore account')


class EditProfileForm(FlaskForm):
    # info card
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('E-mail', validators=[Email()])
    favorite_game = StringField('Favorite Game')
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])

    # main card
    site_link = StringField('Website')
    steam = StringField('Steam')
    twitter = StringField('Twitter')
    instagram = StringField('Instagram')
    facebook = StringField('Facebook')

    submit = SubmitField('Save changes')

    def validate_email(self, email):
        __user = users_repository.get_user(payload={'email': email.data})
        if __user is not None and __user.email != email.data:
            raise ValidationError('The given E-Mail is taken. Use another')


class NewPostCreateForm(FlaskForm):
    title = StringField('Title')
    content = StringField('Text')

    submit = SubmitField('Create')
