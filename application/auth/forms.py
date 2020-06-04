from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import Email, InputRequired, Length
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField("Salasana", validators=[InputRequired(), Length(min=3, max=63)])
  # remember = BooleanField("Muista minut", default=False)
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", validators=[InputRequired(), Length(min=3, max=63)])
    email = StringField("Email", validators=[Email(), InputRequired(), Length(min=3, max=63)])
    username = StringField("Käyttäjätunnus", validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField("Salasana", validators=[InputRequired(), Length(min=3, max=63)])

    class Meta:
        csrf = False