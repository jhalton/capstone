from flask import Blueprint, request
from flask_login import login_required
from .decorators import admin_required
from app.models import Collection, book_collections, db
from app.forms import CreateCollectionForm
from .auth_routes import validation_errors_to_error_messages

collection_routes = Blueprint('collections', __name__)

@collection_routes.route('/')
def all_collections():
    """
    Query for all collections and returns them in a list of dictionaries
    """

    collections = Collection.query.all()
    
    collections_w_books = []
    for collection in collections:
        collection_w_books = collection.to_dict()

        if collection.books:
            collection_w_books['Books'] = [book.to_dict() for book in collection.books]
        else:
            collection_w_books["Books"] = []

        collections_w_books.append(collection_w_books)

    return {'Collections': collections_w_books}


@collection_routes.route('/<int:id>')
def get_collection(id):
    """
    Query for a collection by id
    """
    
    collection = Collection.query.get(int(id))
    if not collection: 
        {'message': "Collection couldn't be found"}, 404
    return {"Books": [book.to_dict_by_id() for book in collection.books]}
    
    



@collection_routes.route('/new', methods=["POST"])
@login_required 
@admin_required
def create_collection():
    """
    Creates a new collection
    """
    form = CreateCollectionForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        collection = Collection(
            name=form.data['name'],
            description=form.data['description']
        )

        db.session.add(collection)
        db.session.commit()
        return collection.to_dict(), 201
    return validation_errors_to_error_messages(form.errors), 400



@collection_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
@admin_required
def edit_collection(id):
    """
    Updates a collection
    """
    form = CreateCollectionForm()
     # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    collection = Collection.query.get(int(id))
    if not collection:
        return {'errors': "Collection couldn't be found"}, 404
    
    if form.validate_on_submit():
        collection.name = form.data['name']
        collection.description = form.data['description']

        db.session.commit()
        return collection.to_dict()
    return validation_errors_to_error_messages(form.errors), 400

@collection_routes.route('/<int:id>/add_books', methods=["PUT"])
@login_required
@admin_required
def add_books_to_collection(id):
    """
    Adds books to a collection
    """
    data = request.get_json()
    book_ids = data.get('book_ids', [])

    for book_id in book_ids:
        book_collection = book_collections.insert().values(collection_id=id, book_id=book_id)
        db.session.execute(book_collection)

    db.session.commit()

    return {'message': "Books successfully added to the collection"}


@collection_routes.route('/<int:id>/delete', methods=["DELETE"])
@login_required
@admin_required
def delete_collection(id):
    """
    Deletes a collection
    """
    collection = Collection.query.get(int(id))
    if not collection:
        return {'errors': "Collection couldn't be found"}, 404
    
    db.session.delete(collection)
    db.session.commit()
    return {'message': "Your collection has been successfully deleted"}

    
    

#--------------------------------Test Admin--------------------------------
@collection_routes.route('/secret')
@admin_required
def the_scottish_endpoint():
    return "Double, double toil and trouble: Fire burn, and cauldron bubble. By the pricking of my thumbs, Something wicked this way comes."


#-------------------------------Books--------------------------------------
@collection_routes.route('/<int:id>/books')
def get_books_by_collection_id(id):
    """
    Query for all books in a collection
    """
    collection = Collection.query.get(int(id))

    if not collection: 
        return {'message': "Collection couldn't be found"}, 404
    
    books_in_collection = collection.books
    return {'Books in collection': [book.to_dict() for book in books_in_collection]}
