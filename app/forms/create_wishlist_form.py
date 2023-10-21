from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional
from app.models import Collection

class CreateWishlistForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Wishlist name is required")], default="New Wishlist")
    