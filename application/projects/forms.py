from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, validators
from datetime import date

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi", [validators.Length(min=3)])
    description = StringField("Kuvaus", [validators.Length(min=3)])
    start_date = DateField("Alkaa", default=date.today)
    end_date = DateField("Päättyy", default=date.today)
    run = BooleanField("Käynnissä")

    def validate_on_submit(self):
        result = super(ProjectForm, self).validate()
        if (self.start_date.data > self.end_date.data):
            return False
        else:
            return result

    class Meta:
        csrf = False