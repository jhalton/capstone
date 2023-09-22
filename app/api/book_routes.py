from flask import Blueprint, request
from flask_login import login_required
from .decorators import admin_required
from app.models import Book, Collection, Review, db
from app.forms import CreateBookForm
from .auth_routes import validation_errors_to_error_messages

book_routes = Blueprint('books', __name__)

@book_routes.route('/')
def all_books():
    """
    Query for all books and returns them in a list of book dictionaries
    """
    books = Book.query.all()
    return {'Books': [book.to_dict() for book in books]}



@book_routes.route('/<int:id>')
def book_detail(id):
    """
    Return book by its id
    """
    book = Book.query.get(int(id))
    if book:
        return book.to_dict_by_id()
    else:
        return {'message': "Book couldn't be found"}, 404
    
    

@book_routes.route('/new', methods=["POST"])
@login_required
@admin_required
def create_book():
    """
    Creates a book
    """
    form = CreateBookForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        book = Book (
            title = form.data['title'],
            author_first_name = form.data['author_first_name'],
            author_last_name = form.data['author_last_name'],
            genre = form.data['genre'],
            format = form.data['format'],
            isbn = form.data['isbn'],
            price = form.data['price'],
            front_image = form.data['front_image'],
            back_image = form.data['back_image'],
            publisher = form.data['publisher'],
            publication_date = form.data['publication_date'],
            on_hand = form.data['on_hand'],
            description = form.data['description']
        )
        db.session.add(book)
        db.session.commit()
        return book.to_dict(), 201
    return validation_errors_to_error_messages(form.errors), 400

@book_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
@admin_required
def edit_book(id):
    """
    Updates a book
    """
    form = CreateBookForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    book = Book.query.get(int(id))
    if not book:
        return {'errors': "Book couldn't be found"}, 404
    
    if form.validate_on_submit():
        book.title = form.data['title']
        book.author_first_name = form.data['author_first_name']
        book.author_last_name = form.data['author_last_name']
        book.genre = form.data['genre']
        book.format = form.data['format']
        book.isbn = form.data['isbn']
        book.price = form.data['price']
        book.front_image = form.data['front_image']
        book.back_image = form.data['back_image']
        book.publisher = form.data['publisher']
        book.publication_date = form.data['publication_date']
        book.on_hand = form.data['on_hand']
        book.description = form.data['description']

        db.session.commit()
        return book.to_dict()
    return validation_errors_to_error_messages(form.errors), 400



@book_routes.route('/<int:id>/delete', methods=["DELETE"])
@login_required
@admin_required
def delete_book(id):
    """
    Deletes a book
    """
    book = Book.query.get(int(id))
    if not book:
        return {'errors': "Book couldn't be found"}, 404
    db.session.delete(book)
    db.session.commit()
    return {'message': 'Your book has been successfully deleted'}




#---------------------------Reviews---------------------------
@book_routes.route('/<int:id>/reviews')
def get_book_reviews(id):
    """
    Query for a book's reviews by book id
    """
    book = Book.query.get(int(id))
    if not book:
        return {'errors': "Book couldn't be found"}, 404
    return {"Reviews": [review.to_dict_book_reviews() for review in book.reviews]}
