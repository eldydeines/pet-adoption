"""Pet Adoption Application"""
"""Eldy Deines"""
"""App incorporates WTForms & Validators"""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, RadioField
from wtforms.validators import NumberRange, URL, Optional, InputRequired


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet's Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog','Dog'), ('porcupine', 'Porcupine')],default="cat")
    photo_url = StringField("Picture URL", validators=[URL(message="Please add a valid URL"), Optional()])
    age = IntegerField("Pet's Age",validators=[NumberRange(min=0,max=30, message="Invalid - age must be between 0 - 30")])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editting pets."""
    photo_url = StringField("Picture URL", validators=[URL(message="Please add a valid URL"), Optional()])
    notes = StringField("Notes")
    available = RadioField("Available",coerce=int,choices=[(1,"Yes"),(0,"No")])