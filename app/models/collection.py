from .db import db, environment, SCHEMA, add_prefix_for_prod
from .book_collections import book_collections

class Collection(db.Model):
    __tablename__ = 'collections'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    books = db.relationship('Book', secondary=book_collections, back_populates='collections')

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name,
            'description': self.description
        }
