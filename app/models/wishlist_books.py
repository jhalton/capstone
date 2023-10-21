from .db import db, environment, SCHEMA, add_prefix_for_prod

wishlist_books = db.Table(
    "wishlist_books",
    db.Model.metadata,
    db.Column("wishlist_id", db.Integer, db.ForeignKey(add_prefix_for_prod("wishlists.id")), primary_key=True),
    db.Column("book_id", db.Integer.db.ForeignKey(add_prefix_for_prod("books.id")), primary_key=True)
)

if environment == "production":
    wishlist_books.schema = SCHEMA
