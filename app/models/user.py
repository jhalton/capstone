from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin






class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    hashed_password = db.Column(db.String(255), nullable=False)
    account_type = db.Column(db.String, nullable=False)
    membership = db.Column(db.Boolean)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'streetAddress': self.street_address,
            'city': self.city,
            'state': self.state,
            'accountType': self.account_type,
            'membership': self.membership
        }
