from app.models import db, Collection, Book, book_collections, environment, SCHEMA
from sqlalchemy.sql import text

def seed_book_collections():
    co1_bo1 = book_collections.insert().values(collection_id=1, book_id=1) #featured
    co1_bo3 = book_collections.insert().values(collection_id=1, book_id=3)
    co1_bo19 = book_collections.insert().values(collection_id=1, book_id=19)
    co2_bo1 = book_collections.insert().values(collection_id=2, book_id=1) #horror
    co2_bo2 = book_collections.insert().values(collection_id=2, book_id=2)
    co2_bo3 = book_collections.insert().values(collection_id=2, book_id=3)
    co2_bo4 = book_collections.insert().values(collection_id=2, book_id=4)
    co2_bo6 = book_collections.insert().values(collection_id=2, book_id=6)
    co3_bo7 = book_collections.insert().values(collection_id=3, book_id=7)#fiction
    co3_bo30 = book_collections.insert().values(collection_id=3, book_id=30)#fiction
    co3_bo28 = book_collections.insert().values(collection_id=3, book_id=28)#fiction
    co3_bo27 = book_collections.insert().values(collection_id=3, book_id=27)#fiction
    co3_bo24 = book_collections.insert().values(collection_id=3, book_id=24)#fiction
    co4_bo31 = book_collections.insert().values(collection_id=4, book_id=31) #romance
    co4_bo32 = book_collections.insert().values(collection_id=4, book_id=32)
    co4_bo33 = book_collections.insert().values(collection_id=4, book_id=33)
    co4_bo34 = book_collections.insert().values(collection_id=4, book_id=34)

    db.session.execute(co1_bo1)
    db.session.execute(co1_bo3)
    db.session.execute(co1_bo19)
    db.session.execute(co2_bo1)
    db.session.execute(co2_bo2)
    db.session.execute(co2_bo3)
    db.session.execute(co2_bo4)
    db.session.execute(co2_bo6)
    db.session.execute(co4_bo31)
    db.session.execute(co4_bo32)
    db.session.execute(co4_bo33)
    db.session.execute(co4_bo34)
    db.session.execute(co3_bo7)
    db.session.execute(co3_bo30)
    db.session.execute(co3_bo28)
    db.session.execute(co3_bo27)
    db.session.execute(co3_bo24)
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
