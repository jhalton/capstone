from .db import db, environment, SCHEMA, add_prefix_for_prod
from .wishlist_books import wishlist_books

class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    

    books = db.relationship('Book', secondary=wishlist_books, back_populates='wishlists')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'userId': self.user_id,
           
        }
