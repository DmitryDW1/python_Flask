from random import choices
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('<PASSWORD>', validators=[DataRequired()])
    
    
class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = StringField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский]')])
    
    