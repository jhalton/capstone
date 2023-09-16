from .db import db, environment, SCHEMA, add_prefix_for_prod

class Cart(db.Model):
    __tablename__ = 'carts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('books.id')), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'bookId': self.book_id
        }
