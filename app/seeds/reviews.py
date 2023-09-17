from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    review1 = Review (
        rating=5,
        review="This is the scariest book I've ever read. I read this book while home alone. Big mistake! Loved it!",
        user_id=1,
        book_id=1,
        spoiler=False,
        pen_name=None
    )
    review2 = Review (
        rating=5,
        review="The perfect ghost story. Subtle and suspenseful",
        user_id=2,
        book_id=1,
        spoiler=False,
        pen_name=None
    )
    review3 = Review (
        rating=4,
        review="I thought the story was good, but there have definitely been much better things written recently. It feels a little old to me, you know? Still cool though",
        user_id=3,
        book_id=1,
        spoiler=False,
        pen_name=None
    )
    review4 = Review (
        rating=5,
        review="Frankenstein by Mary Shelley truly deserves its reputation as a defining piece of gothic horror. The story is steeped in suspense and dread for what Frankenstein has created, and it is this foreboding rather than descriptions of the monster that give the greatest sense of horror in the book.",
        user_id=1,
        book_id=2,
        spoiler=False,
        pen_name=None
    )
    review5 = Review (
        rating=4,
        review="Very good obviously (It's Frankenstein), but there's this type on page 65 in chapter 7 of volume 1, saying 'you presence' instead of 'your presence'. It's a very tiny thing and not really an issue but it just sticks with me and I need to vent somewhere.",
        user_id=2,
        book_id=2,
        spoiler=False,
        pen_name=None
    )
    review6 = Review (
        rating=2,
        review="170 pages describing the Swiss Alps and, oh by the way, a guy created a monster. Honest. You just read Frankenstein. There are only a few sentences regarding the creation of the monster. The rest of the book is about the weather (and moral lessons regarding the consequences of our actions, I suppose). Frankenstein is not a horror story.",
        user_id=3,
        book_id=2,
        spoiler=False,
        pen_name=None
    )
    review7 = Review (
        rating=3,
        review="I read Something Wicked This Way Comes by Ray Bradbury because I needed to find a book for my highschool english class. This book has a very interesting plot with a lot of twists and turns, but it was by far not my favorite book in the world. The only reason I feel this way is because I don't like Bradbury's writing style; I find it difficult and bizarre.",
        user_id=1,
        book_id=3,
        spoiler=False,
        pen_name=None
    )
    review8 = Review (
        rating=4,
        review="I thought the book was pretty good. In the beginning the book was a little confusing,but the book played it's self out. The books two main characters names are Jim and Will. A carnival comes late in the season but there is something wicked about it. The crazy illisutionist, Mr. Dark, has something wrong with him. He doesnt really seem normal. There is also the evil partner in crime, The Dust Witch. She is blind but senses thing like see can see. The novel has alot of twist and turns and keeps the reader very interested.I believe that Ray Bradury has made another novel that will last throughtout the ages.",
        user_id=2,
        book_id=3,
        spoiler=False,
        pen_name=None
    )

     



    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()
