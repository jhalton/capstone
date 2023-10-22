from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Wishlist, wishlist_books, db, Book
from .auth_routes import validation_errors_to_error_messages
from app.forms import CreateWishlistForm

wishlist_routes = Blueprint('wishlists', __name__)

@wishlist_routes.route('/')
@login_required
def all_wishlists():
    """
    Query for all of a current user's wishlists
    """

    wishlists = Wishlist.query.filter(wishlist.user_id == current_user.id).all()

    wishlists_w_books = []
    for wishlist in wishlists:
        wishlist_w_books = wishlist.to_dict()

        if wishlist.books:
            wishlist_w_books['Books'] = [book.to_dict() for book in wishlist.books]
        else:
            wishlist_w_books['Books'] = []

        wishlists_w_books.append(wishlists_w_books)

    return {'Wishlists': wishlists_w_books}



@wishlist_routes.route('/<int:id>')
@login_required
def get_wishlist(id):
    """
    Query for a wishlist by id
    """

    wishlist = Wishlist.query.get(int(id))
    if current_user.id != wishlist.user_id:
        return {"message": "You can only access your own wishlists"}, 403
    if not wishlist:
        return {'message': "Wishlist couldn't be found"}, 404
    return {"Wishlist": wishlist.to_dict(), "Books": [book.to_dict_by_id() for book in wishlist.books]}


@wishlist_routes.route('/new', methods=["POST"])
@login_required
def create_wishlist():
    """
    Creates a new wishlist
    """
    form = CreateWishlistForm()
     # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        wishlist = Wishlist(
            name = form.data['name'],
            user_id = current_user.id
        )

        db.session.add(wishlist)
        db.session.commit()
        return wishlist.to_dict(), 201
    return validation_errors_to_error_messages(form.errors), 400


@wishlist_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
def edit_wishlist(id):
    """
    Udates a wishlist
    """
    form = CreateWishlistForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    wishlist = Wishlist.query.get(int(id))
    if wishlist.user_id != current_user.id:
        return {"message": "You can only edit your own wishlists"}, 403
    if not wishlist:
        return {"message": "Wishlist couldn't be found"}, 404
    
    if form.validate_on_submit():
        wishlist.name = form.data['name']

        db.session.commit()
        return wishlist.to_dict()
    return validation_errors_to_error_messages(form.errors), 400


@wishlist_routes.route('/<int:id>/add_books', methods={"PUT"})
@login_required
def add_books_to_wishlist(id):
    """
    Adds books to a wishlist
    """
    data = request.get_json()
    book_ids = data.get('book_ids', [])

    for book_id in book_ids:
        wishlist = wishlist_books.insert().values(wishlist_id=id, book_id=book_id)
        db.session.execute(wishlist)

    db.session.commit()

    return {'message': "Books successfully added to the wishlist"}, 201


@wishlist_routes.route('/<int:id>/<int:bookId>/delete', methods=['DELETE'])
@login_required
def delete_books_from_wishlist(id, bookId):
    """
    Deletes a book from a wishlist
    """
    wishlist = Wishlist.query.get(int(id))
    book = Book.query.get(int(bookId))
    if wishlist.user_id != current_user.id:
        return {"message": "You can only remove books from your own collections"}, 403
    if not wishlist:
        return {"message": "Wishlist couldn't be found"}, 404
    
    if book in wishlist.books:
        wishlist.books.remove(book)
        db.session.commit()
        return {'message': 'Book was successfully remove from this collection'}
    else:
        return {"message": "Book is not in this collection"}, 400
    


@wishlist_routes.route('/<int:id>/delete', methods=["DELETE"])
@login_required
def delete_wishlist():
    """
    Deletes a wishlist
    """

    wishlist = Wishlist.query.get(int(id))
    if wishlist.user_id != current_user.id:
        return {"message": "You can only delete books from your own wishlist"}, 403
    if not wishlist:
        return {'message': "Wishlist couldn't be found"}, 404
    
    db.session.delete(wishlist)
    db.session.commit()
    return {"message": "Your wishlist was successfully deleted"}



#-------------------------------Books--------------------------------------
@wishlist_routes.route('/<int:id>/books')
@login_required
def get_books_by_wishlist_id(id):
    """
    Query for all books in a wishlist
    """
    wishlist = Wishlist.query.get(int(id))

    if wishlist.user_id != current_user.id:
        return {"message": "You can only view your own wishlists"}, 403
    if not wishlist:
        return {"message": "Wishlist couldn't be found"}, 404
    
    books_in_wishlist = wishlist.books
    return {"Books in wishlist": [book.to_dict() for book in books_in_wishlist]}
