from flask import Blueprint
from flask_login import login_required
from app.models import Collection

collection_routes = Blueprint('collections', __name__)

@collection_routes.route('/')
def all_collections():
    """
    Query for all collections and returns them in a list of dictionaries
    """

    collections = Collection.query.all()
    # return "HELLO! FROM COLLECTIONS!"
    return {'collections': [collection.to_dict() for collection in collections]}
