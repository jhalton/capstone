from app.models import db, Book, environment, SCHEMA
from sqlalchemy.sql import text

#Adds books to the database
def seed_books():
    haunting_of_hill_house = Book(
        title="The Haunting of Hill House", 
        author_first_name="Shirley",
        author_last_name="Jackson", 
        genre="horror",
        format="paperback",
        isbn="9780143039983",
        price=14.99,
        front_image="https://m.media-amazon.com/images/I/51PT+eAwsVL._SY445_SX342_.jpg",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2006-11-28",
        on_hand=10
    )
    

    db.session.add(haunting_of_hill_house)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_books():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.books RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM books"))
        
    db.session.commit()
