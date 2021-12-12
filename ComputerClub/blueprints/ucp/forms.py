from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo

from ComputerClub.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('E-mail', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, _username):
        _user = User.query.filter_by(username=_username.data).first()
        if _user is not None:
            raise ValidationError('The given username is taken. Use another')

    def validate_email(self, _email):
        _user = User.query.filter_by(email=_email.data).first()
        if _user is not None:
            raise ValidationError('The given E-Mail is taken. Use another')


# todo create RecoveryForm
class RecoveryForm(FlaskForm):
    pass
