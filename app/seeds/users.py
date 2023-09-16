from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name='Demo',last_name='User',  email='demo@aa.io', phone='1111111111', street_address=None, city=None, state=None,  password='password', account_type="Consumer", membership=True)
    marnie = User(
        first_name='Marnie',last_name='Cromwell',  email='marnie@aa.io', phone='2222222222', street_address=None, city=None, state=None,  password='password', account_type="Consumer", membership=True)
    bobbie = User(
        first_name='Bobbie',last_name='Markowe',  email='bobbie@aa.io', phone='3333333333', street_address=None, city=None, state=None,  password='password', account_type="Consumer", membership=False)
    admin = User(
        first_name='Admin',last_name='User',  email='admin@aa.io', phone='4444444444', street_address=None, city=None, state=None,  password='password', account_type="Admin", membership=True)
    

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(admin)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
