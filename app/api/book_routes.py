from flask import Blueprint
from flask_login import login_required
from app.models import Book, Collection, Review

book_routes = Blueprint('books', __name__)

@book_routes.route('/')
def all_books():
    """
    Query for all books and returns them in a list of book dictionaries
    """
    books = Book.query.all()
    return {'books': [book.to_dict() for book in books]}



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


#---------------------------Reviews---------------------------
@book_routes.route('/<int:id>/reviews')
def get_book_reviews(id):
    """
    Query for a book's reviews by book id
    """
    book = Book.query.get(int)
    if not book:
        return {'errors': "Book couldn't be found"}, 404
    return {"Reviews": [review.to_dict_book_reviews()] for review in book.reviews}
