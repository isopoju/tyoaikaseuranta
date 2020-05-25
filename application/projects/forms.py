from flask_wtf import FlaskForm
from wtforms import StringField, DateField

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi")
    # kuvaus = StringField("Kuvaus")
    # alku = DateField("Alku pvm")
    # loppu = DateField("Loppu pvm")
 
    class Meta:
        csrf = False