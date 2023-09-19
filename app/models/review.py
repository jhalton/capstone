from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('books.id')), nullable=False)
    spoiler = db.Column(db.Boolean, nullable=False)
    pen_name = db.Column(db.String)

    book = db.relationship(
        'Book', back_populates='reviews')


    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'review': self.review,
            'userId': self.user_id,
            'bookId': self.book_id,
            'spoiler': self.spoiler,
            'penName': self.pen_name
        }
    
    def to_dict_book_reviews(self):
        review = self.to_dict()
        review["Book"] = self.book.to_dict_review()
        return review
    
    
    
        
