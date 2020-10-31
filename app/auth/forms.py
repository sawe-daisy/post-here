from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, EqualTo, Email
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Enter Your Email Address', validators=[Required(),Email()])
    username = StringField("Enter Your Username", validators=[Required()])
    password = PasswordField('Your password', validators=[Required(),EqualTo('password_confirm', message='Passwords must be identical')])
    password_confirm =PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email= data_field.data).first():
            raise ValidationError('That username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(), Email()])
    password = PasswordField('Enter your password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')