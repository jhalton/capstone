from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')
    
def phone_number_exists(form, field):
    # Checking of phone_number is already in use
    phone = field.data
    user = User.query.filter(User.phone == phone).first()
    if user:
        raise ValidationError('Phone number already in use.')





class SignUpForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), user_exists])
    phone = StringField("Phone number", validators=[DataRequired(), phone_number_exists])
    street_address = StringField("Street address")
    city = StringField("City")
    state = StringField("State")
    account_type = SelectField("Account type", choices=["Admin", "Consumer"], default='Consumer', validators=[DataRequired()])
    membership = BooleanField("Membership")
    password = StringField('Password', validators=[DataRequired()])
