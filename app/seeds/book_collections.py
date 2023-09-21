from app.models import db, Collection, Book, book_collections, environment, SCHEMA
from sqlalchemy.sql import text

def seed_book_collections():
    co2_bo1 = book_collections.insert().values(collection_id=2, book_id=1)
    co2_bo2 = book_collections.insert().values(collection_id=2, book_id=3)
    co2_bo3 = book_collections.insert().values(collection_id=2, book_id=6)

    db.session.execute(co2_bo1)
    db.session.execute(co2_bo2)
    db.session.execute(co2_bo3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_book_collections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.book_collections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM book_collections"))
        
    db.session.commit()
