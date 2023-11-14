from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Review, Book, db
from app.forms import CreateReviewForm
from .auth_routes import validation_errors_to_error_messages

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




@review_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
def edit_book_review(id):
    """
    Updates an existing book review
    """
    form = CreateReviewForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    review = Review.query.get(int(id))
    if not review:
        return {'errors': "Review couldn't be found"}, 404
    
    if form.validate_on_submit():
        review.rating = form.data['rating']
        review.review = form.data['review']
        review.spoiler = form.data['spoiler']
        review.pen_name = form.data['pen_name']

        db.session.commit()
        return review.to_dict()
    return validation_errors_to_error_messages(form.errors), 400


@review_routes.route("/<int:id>/delete", methods=["DELETE"])
@login_required
def delete_book_review():
    """
    Deletes a book review
    """
    review = Review.query.get(int(id))
    if not review:
        return {'errors', "Review couldn't be found"}, 400
    db.session.delete(review)
    db.session.commit()
    return {'message': "Your review has been successfully deleted"}

        
    
    
