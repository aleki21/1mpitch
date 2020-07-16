from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from .forms import UpdateProfile
from .. import db

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class addPitch(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    category = SelectField("What is the type of pitch", choices=[("funny", "funny"), ("brainy", "brainy"), ("romantic", "romantic"), ("inspirational", "inspirational"),( "random", "random"), ("business", "business"), ("spiritual", "spiritual")],validators=[Required()])
    description = TextAreaField("Enter Pitch", validators = [Required()])
    submit = SubmitField("Add Pitch")