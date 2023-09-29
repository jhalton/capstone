from app.models import db, Collection, environment, SCHEMA
from sqlalchemy.sql import text

def seed_collections():
    featured = Collection(
        name='Featured',
        description='Our current staff picks featured to inspire your next adventure!'
    )
    horror = Collection(
        name='Horror',
        description='If you like to be disturbed, frightened, or scared, then surely there will be something in this collection for you.'
    )
    fiction = Collection(
        name='Fiction',
        description="General fiction is a broad category for writing that doesn't quite fit any particular genre. Here you'll find books that usually deal with real, contemporary settings and recognizable characters."
    )
    romance = Collection (
        name="Romance",
        description="In our romance section you'll find books that are like a roller-coaster for your heart! Whether it's love at first sight, rekindling old flames, or overcoming quirky obstacles, these novels promise an emotional joyride with happy-ever-after as the ultimate destination. "
    )
    nonfiction = Collection (
        name="Nonfiction",
        description="Here you'll find books that are a window to the real world, offering a wealth of knowledge, insights, and true stories."
    )
    young_adult = Collection (
        name="Young Adult",
        description="Here you'll find books that are vibrant and dynamic, specifically tailored for teenagers and young adults. Explore the complexities of adolescence, self-discovery, and personal growth."
    )
    autobiography = Collection (
        name="Autobiography",
        description="Here you'll find an intimate glimpse into the life journey of an individual narrated by the person themselves. These books recount the author's life experiences, trials, triumphs, and refections, offering a firsthand account of their unique path."
    )
    personal_development = Collection(
        name="Personal Development",
        description="Like compasses for self-improvement, these books guide readers on a transformation journey towards becoming the best version of themselves. These books delve into a plethora of topics aimed at enhancing one's mindset, skills, habits, and overall life satisfaction. From goal-setting and time management to emotional intelligence and self-awareness, personal development literature offers actionable adivce, exercises, and strategies to empower individuals to achieve their potential and lead a more fulfilling life."
    )
    science_fiction = Collection(
        name="Science Fiction",
        description="Science fiction books propel readers into fascinating worlds of imagination and futuristic innovation. These novels are a captivating blend of scientific possibilities, speculative concepts, and advanced technologies, often set in futuristic or otherworldly environments. "
    )
    fantasy = Collection (
        name="Fantasy",
        description="Fantasy books transport readers into magical realms where the impossible becomes reality. These captivating stories are steeped in imagination and often set in fictional worlds filled with mystical creatures, magic, quests, and epic battles between good and evil."
    )



    db.session.add(featured) #1
    db.session.add(horror) #2
    db.session.add(fiction) #3
    db.session.add(romance) #4
    db.session.add(nonfiction) #5
    db.session.add(young_adult) #6
    db.session.add(autobiography) #7
    db.session.add(personal_development) #8
    db.session.add(science_fiction) #9
    db.session.add(fantasy) #10
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
