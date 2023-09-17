from .db import db, environment, SCHEMA, add_prefix_for_prod
from .book_collections import book_collections

class Book(db.Model):
    __tablename__ = 'books'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author_first_name = db.Column(db.String, nullable=False)
    author_last_name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    format = db.Column(db.String)
    isbn = db.Column(db.String)
    price = db.Column(db.Float)
    front_image = db.Column(db.String)
    back_image = db.Column(db.String)
    publisher = db.Column(db.String)
    publication_date = db.Column(db.String)
    on_hand = db.Column(db.Integer)
    description = db.Column(db.String)


    collections = db.relationship('Collection', secondary=book_collections, back_populates='books')

    def to_dict(self):
        return {
            'id': self.id, 
            'title': self.title, 
            'authorFirstName': self.author_first_name, 
            'authorLastName': self.author_last_name, 
            'genre': self.genre,
            'format':self.format,
            'isbn': self.isbn, 
            'price': self.price, 
            'frontImage': self.front_image,
            'backImage': self.back_image,
            'publisher': self.publisher,
            'publicationDate': self.publication_date,
            'onHand': self.on_hand,
            'description': self.description
        }


    def to_dict_by_id(self):
        book = self.to_dict()
        if self.reviews:
            avg_rating = round(sum(review.rating for review in self.reviews) / len(self.review), 1)
            book["avgRating"] = avg_rating
        else:
            book['avgRating'] = None
        book['numRatings'] = len(self.reviews)
        return book
