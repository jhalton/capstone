from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, BooleanField

class CreateReviewForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired()])
    review = StringField("Review")
    spoiler = BooleanField("Spoilers", validators=[DataRequired()])
    pen_name = StringField("Pen name")
