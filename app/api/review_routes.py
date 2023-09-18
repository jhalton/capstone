from flask import Blueprint
from flask_login import login_required
from app.models import Review

review_routes = Blueprint('reviews', __name__)


@review_routes.route('/<int:id>')
def review_by_id(id):
    """
    Query for review by id
    """
    review = Review.query.get(int(id))
    if review:
        return review.to_dict()
    else: 
        {'message': "Review couldn't be found"}, 404
