from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class AddPropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedrooms = StringField('Number of Bedrooms', validators=[InputRequired()])
    bathrooms = StringField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only Static Images Allowed')]) 