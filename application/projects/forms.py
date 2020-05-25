from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi")
    ended = BooleanField("Päättynyt")
    # kuvaus = StringField("Kuvaus")
    # alku = DateField("Alku pvm")
    # loppu = DateField("Loppu pvm")
 
    class Meta:
        csrf = False