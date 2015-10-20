from flask.ext.wtf import Form
from wtforms import DecimalField, validators

class GasLaw(Form):
    pressure = DecimalField('Pressure', validators=[validators.optional()])
    volume = DecimalField('Volume', validators=[validators.optional()])
    temperature = DecimalField('Temperature', validators=[validators.optional()])
