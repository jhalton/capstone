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
    co3_bo16 = book_collections.insert().values(collection_id=3, book_id=16)#fiction
    co3_bo17 = book_collections.insert().values(collection_id=3, book_id=17)#fiction
    co3_bo21 = book_collections.insert().values(collection_id=3, book_id=21)#fiction
    co3_bo22 = book_collections.insert().values(collection_id=3, book_id=22)#fiction
    co3_bo24 = book_collections.insert().values(collection_id=3, book_id=24)#fiction
    co3_bo27 = book_collections.insert().values(collection_id=3, book_id=27)#fiction
    co3_bo28 = book_collections.insert().values(collection_id=3, book_id=28)#fiction
    co3_bo30 = book_collections.insert().values(collection_id=3, book_id=30)#fiction
    co4_bo31 = book_collections.insert().values(collection_id=4, book_id=31) #romance
    co4_bo32 = book_collections.insert().values(collection_id=4, book_id=32)
    co4_bo33 = book_collections.insert().values(collection_id=4, book_id=33)
    co4_bo34 = book_collections.insert().values(collection_id=4, book_id=34)
    co5_bo35 = book_collections.insert().values(collection_id=5, book_id=35) #nonfiction
    co5_bo36 = book_collections.insert().values(collection_id=5, book_id=36) #nonfiction
    co5_bo37 = book_collections.insert().values(collection_id=5, book_id=37) #nonfiction
    co5_bo38 = book_collections.insert().values(collection_id=5, book_id=38) #nonfiction
    co5_bo39 = book_collections.insert().values(collection_id=5, book_id=39) #nonfiction
    co7_bo40 = book_collections.insert().values(collection_id=7, book_id=40) #autobiography
    co7_bo41 = book_collections.insert().values(collection_id=7, book_id=41) #autobiography
    co7_bo42 = book_collections.insert().values(collection_id=7, book_id=42) #autobiography
    co7_bo43 = book_collections.insert().values(collection_id=7, book_id=43) #autobiography
    co6_bo44 = book_collections.insert().values(collection_id=6, book_id=44) #young adult
    co6_bo45 = book_collections.insert().values(collection_id=6, book_id=45) #young adult
    co6_bo46 = book_collections.insert().values(collection_id=6, book_id=46) #young adult
    co6_bo47 = book_collections.insert().values(collection_id=6, book_id=47) #young adult
    co6_bo48 = book_collections.insert().values(collection_id=6, book_id=48) #young adult
    co8_bo11 = book_collections.insert().values(collection_id=8, book_id=11) #personal growth
    co8_bo12 = book_collections.insert().values(collection_id=8, book_id=12) #personal growth
    co8_bo13 = book_collections.insert().values(collection_id=8, book_id=13) #personal growth
    co8_bo14 = book_collections.insert().values(collection_id=8, book_id=14) #personal growth
    co8_bo15 = book_collections.insert().values(collection_id=8, book_id=15) #personal growth
    co9_bo10 = book_collections.insert().values(collection_id=9, book_id=10) #science fiction
    co9_bo29 = book_collections.insert().values(collection_id=9, book_id=29) #science fiction
    co9_bo49 = book_collections.insert().values(collection_id=9, book_id=49) #science fiction
    co9_bo50 = book_collections.insert().values(collection_id=9, book_id=50) #science fiction
    co10_bo25 = book_collections.insert().values(collection_id=10, book_id=25) #fantasy
    co10_bo51 = book_collections.insert().values(collection_id=10, book_id=51) #fantasy
    co10_bo52 = book_collections.insert().values(collection_id=10, book_id=52) #fantasy
    co10_bo53 = book_collections.insert().values(collection_id=10, book_id=53) #fantasy
    co10_bo54 = book_collections.insert().values(collection_id=10, book_id=54) #fantasy
    co10_bo55 = book_collections.insert().values(collection_id=10, book_id=55) #fantasy
    co10_bo56 = book_collections.insert().values(collection_id=10, book_id=56) #fantasy
    co10_bo57 = book_collections.insert().values(collection_id=10, book_id=57) #fantasy
    co10_bo58 = book_collections.insert().values(collection_id=10, book_id=58) #fantasy


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
    db.session.execute(co5_bo35)
    db.session.execute(co5_bo36)
    db.session.execute(co5_bo37)
    db.session.execute(co5_bo38)
    db.session.execute(co5_bo39)
    db.session.execute(co7_bo40)
    db.session.execute(co7_bo41)
    db.session.execute(co7_bo42)
    db.session.execute(co7_bo43)
    db.session.execute(co6_bo44)
    db.session.execute(co6_bo45)
    db.session.execute(co6_bo46)
    db.session.execute(co6_bo47)
    db.session.execute(co6_bo48)
    db.session.execute(co8_bo11)
    db.session.execute(co8_bo12)
    db.session.execute(co8_bo13)
    db.session.execute(co8_bo14)
    db.session.execute(co8_bo15)
    db.session.execute(co9_bo10)
    db.session.execute(co9_bo29)
    db.session.execute(co9_bo49)
    db.session.execute(co9_bo50)
    db.session.execute(co10_bo25)
    db.session.execute(co10_bo51)
    db.session.execute(co3_bo16)
    db.session.execute(co3_bo17)
    db.session.execute(co3_bo21)
    db.session.execute(co3_bo22)
    db.session.execute(co10_bo52)
    db.session.execute(co10_bo53)
    db.session.execute(co10_bo54)
    db.session.execute(co10_bo55)
    db.session.execute(co10_bo56)
    db.session.execute(co10_bo57)
    db.session.execute(co10_bo58)
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
