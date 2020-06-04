from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange
from datetime import date

class WorkloadForm(FlaskForm):
    date = DateField("Päivämäärä", default=date.today, format='%Y-%m-%d', validators=[InputRequired()])
    hours = IntegerField("Tunnit", default=1, validators=[DataRequired(), NumberRange(1,24)])
    task = StringField("Tehtävä", validators=[InputRequired(), Length(min=3, max=127)])

    class Meta:
        csrf = False