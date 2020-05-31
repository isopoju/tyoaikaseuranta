from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.Length(min=3)])

    class Meta:
        csrf = False