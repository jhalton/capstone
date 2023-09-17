from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Book


def book_exists(form, field):
    #Checking if ISBN is already in the store
    isbn = field.data
    book = Book.query.filter(Book.isbn == isbn).first()
    if book:
        raise ValidationError('A book with this ISBN is already in your store.')

class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author_first_name = StringField("First name", validators=[DataRequired()])
    author_last_name = StringField("Last name", validators=[DataRequired()])
    genre = StringField("Genre")
    format = StringField("Format")
    isbn = StringField("ISBN")
    price = FloatField("Price", validators=[DataRequired()])
    front_image = StringField("Front cover")
    back_image = StringField("Back cover")
    publisher = StringField("Publisher")
    publication_date = StringField("Publication date")
    on_hand = IntegerField("On hand", validators=[DataRequired()])
    description = StringField("Overview")
