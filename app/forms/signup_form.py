from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, EmailField
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

def phone_number_length(form, field):
    # Checking to make sure phone number is proper length
    phone_number = field.data
    if len(phone_number) < 10:
        raise ValidationError("Phone number must be 10 digits")



class SignUpForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired("First name is required")])
    last_name = StringField("Last name", validators=[DataRequired("Last name is required")])
    email = EmailField('Email', validators=[DataRequired("Email is required"), user_exists, Email("Please enter a valid email address")])
    phone = StringField("Phone number", validators=[DataRequired("Phone number is required"), phone_number_exists, phone_number_length])
    street_address = StringField("Street address")
    city = StringField("City")
    state = StringField("State")
    account_type = SelectField("Account type", choices=["Admin", "Consumer"], default='Consumer', validators=[DataRequired()])
    membership = BooleanField("Membership")
    password = StringField('Password', validators=[DataRequired("Password is required")])
