from .db import db, environment, SCHEMA, add_prefix_for_prod

book_collections = db.Table(
    "book_collections",
    db.Model.metadata,
    db.Column('collection_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod('collections.id')), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod('books.id')), primary_key=True)
)


if environment == "production":
    book_collections.schema = SCHEMA
