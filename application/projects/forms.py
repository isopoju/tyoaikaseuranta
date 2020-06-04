from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators
from wtforms.fields.html5 import DateField
from datetime import date

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi", [validators.Length(min=3)])
    description = StringField("Kuvaus", [validators.Length(min=3)])
    start_date = DateField("Alkaa", default=date.today, format='%Y-%m-%d')
    end_date = DateField("Päättyy", default=date.today, format='%Y-%m-%d')
    running = BooleanField("Käynnissä")

    def validate_dates(self):
        result = super(ProjectForm, self).validate()
        if (self.start_date.data > self.end_date.data):
            return False
        else:
            return result

    class Meta:
        csrf = False