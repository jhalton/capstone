from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional
from app.models import Book


def book_exists(form, field):
    #Checking if ISBN is already in the store
    isbn = field.data
    book_id = form.book_id.data

    if book_id:
       existing_book = Book.query.filter(
           Book.isbn == isbn,
           Book.id != book_id

       ).first()
       if existing_book:
           raise ValidationError("A book with this ISBN is already in your store")
       else:
           existing_book = Book.query.filter_by(isbn=isbn).first()
           if existing_book:
               raise ValidationError("A book with this ISBN is already in your store")

    # book = Book.query.filter(Book.isbn == isbn, Book.id != book_id).first()
    # if book:
    #     raise ValidationError('A book with this ISBN is already in your store')
    

def min_price(form, field):
    # Checks if price is $0.00 or more
    price = field.data

    if price <= 0:
        raise ValidationError("Price must be more than $0.00")
    

def min_on_hand(form, field):
    # Checks is on hand is 0 or more
    on_hand = field.data

    if on_hand < 0:
        raise ValidationError("On hand quantity cannot be less than 0")
    

    


class CreateBookForm(FlaskForm):
    book_id = IntegerField("Book ID", validators=[Optional()])
    title = StringField('Title', validators=[DataRequired("Title is required")])
    author_first_name = StringField("First name", validators=[DataRequired("Author's first name is required")])
    author_last_name = StringField("Last name", validators=[DataRequired("Author's last name is required")])
    genre = StringField("Genre")
    format = StringField("Format")
    isbn = StringField("ISBN", validators=[DataRequired("ISBN is required"), book_exists])
    price = FloatField("Price", validators=[DataRequired("Price is required"), min_price])
    front_image = StringField("Front cover", validators=[DataRequired("Cover image is required")])
    back_image = StringField("Back cover")
    publisher = StringField("Publisher")
    publication_date = StringField("Publication date")
    on_hand = IntegerField("On hand", validators=[DataRequired("On hand is required"), min_on_hand])
    description = StringField("Overview")
