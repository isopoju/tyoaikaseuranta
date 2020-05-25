from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, validators

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi", [validators.Length(min=2)])
    ended = BooleanField("Päättynyt")
    # kuvaus = StringField("Kuvaus")
    # alku = DateField("Alku pvm")
    # loppu = DateField("Loppu pvm")
 
    class Meta:
        csrf = False