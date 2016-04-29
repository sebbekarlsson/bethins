from wtforms import (
    BooleanField,
    TextField,
    TextAreaField,
    PasswordField,
    validators,
    SubmitField,
    FileField,
    IntegerField
)
from wtforms.fields.html5 import EmailField
from flask.ext.wtf import Form


class LoginForm(Form):
    user_name = TextField('User Name', [validators.Length(min=4, max=35)])
    password = PasswordField('Password', [
        validators.Required()
    ])
    submit = SubmitField('Login')


class UploadFileForm(Form):
    file = FileField('File')
    submit = SubmitField('Upload')


class UserForm(Form):
    email = EmailField('Email', [validators.Length(min=4, max=35)])
    user_name = TextField('User Name', [validators.Length(min=4, max=35)])
    password = TextField('Choose Password', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = TextField('Repeat Password')
    submit = SubmitField('Register')
