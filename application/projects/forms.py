from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length
from datetime import date

class ProjectForm(FlaskForm):
    name = StringField("Projektin nimi", validators=[InputRequired(), Length(min=3, max=127)])
    description = StringField("Kuvaus", validators=[InputRequired(), Length(min=3, max=1023)])
    start_date = DateField("Alkaa", default=date.today, format='%Y-%m-%d', validators=[InputRequired()])
    end_date = DateField("Päättyy", default=date.today, format='%Y-%m-%d', validators=[InputRequired()])
    running = BooleanField("Käynnissä")

    def validate_dates(self):
        result = super(ProjectForm, self).validate()
        if (self.start_date.data > self.end_date.data):
            return False
        else:
            return result

    class Meta:
        csrf = False