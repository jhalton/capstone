from app.models import db, Collection, environment, SCHEMA
from sqlalchemy.sql import text

def seed_collections():
    horror = Collection(
        name='Horror',
        description='If you like to be disturbed, frightened, or scared, then surely there will be something in this collection for you.'
    )
    featured = Collection(
        name='Featured',
        description='Our current staff picks featured to inspire your next adventure!'
    )


    db.session.add(horror)
    db.session.add(featured)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_collections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collections"))
        
    db.session.commit()
