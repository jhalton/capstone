from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class CreateReviewForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired()])
    review = StringField("Review")
    spoiler = BooleanField("Spoilers", validators=[DataRequired()])
    pen_name = StringField("Pen name")
