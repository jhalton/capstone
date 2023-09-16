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
        on_hand=10,
        description="First published in 1959, Shirley Jackson's The Haunting of Hill House has been hailed as a perfect work of unnerving terror. It is the story of four seekers who arrive at a notoriously unfriendly pile called Hill House: Dr. Montague, an occult scholar looking for solid evidence of a “haunting”; Theodora, his lighthearted assistant; Eleanor, a friendless, fragile young woman well acquainted with poltergeists; and Luke, the future heir of Hill House. At first, their stay seems destined to be merely a spooky encounter with inexplicable phenomena. But Hill House is gathering its powers—and soon it will choose one of them to make its own."
    )
    frankenstein = Book(
        title="Frankenstein", 
        author_first_name="Mary",
        author_last_name="Shelley", 
        genre="horror",
        format="paperback",
        isbn="9781435159624",
        price=15.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781435159624_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Barnes and Noble",
        publication_date="2015-03-20",
        on_hand=10,
        description="Stepping far afield from his medical studies, Victor Frankenstein brings to life a human form he has fashioned from scavenged body parts. Horrified by his achievement, he turns his back on his creation, only to learn the danger of such neglect. Written when Mary Shelley was only 20 years old, Frankenstein has been hailed as both a landmark of Gothic horror fiction and the first modern science fiction story."
    )
    something_wicked_this_way_comes = Book(
        title="Something Wicked This Way Comes", 
        author_first_name="Ray",
        author_last_name="Bradbury", 
        genre="horror",
        format="paperback",
        isbn="9781501167713",
        price=17.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781501167713_p0_v6_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Simon and Schuster",
        publication_date="2017-10-24",
        on_hand=10,
        description="For those who still dream and remember, for those yet to experience the hypnotic power of its dark poetry, step inside. The show is about to begin. Cooger & Dark's Pandemonium Shadow Show has come to Green Town, Illinois, to destroy every life touched by its strange and sinister mystery. The carnival rolls in sometime after midnight, ushering in Halloween a week early. A calliope’s shrill siren song beckons to all with a seductive promise of dreams and youth regained. Two boys will discover the secret of its smoke, mazes, and mirrors; two friends who will soon know all too well the heavy cost of wishes...and the stuff of nightmares."
    )
    slade_house = Book(
        title="Slade House", 
        author_first_name="David",
        author_last_name="Mitchell", 
        genre="horror",
        format="paperback",
        isbn="9780812988079",
        price=17.00,
        front_image="https://m.media-amazon.com/images/I/61XFC6g4ruL._SY445_SX342_.jpg",
        back_image=None,
        publisher="Random House Publishing Group",
        publication_date="2016-06-28",
        on_hand=10,
        description="Keep your eyes peeled for a small black iron door.Down the road from a working-class British pub, along the brick wall of a narrow alley, if the conditions are exactly right, you'll find the entrance to Slade House. A stranger will greet you by name and invite you inside. At first, you won't want to leave. Later, you'll find that you can't. Every nine years, the house's residents—an odd brother and sister—extend a unique invitation to someone who's different or lonely: a precocious teenager, a recently divorced policeman, a shy college student. But what really goes on inside Slade House? For those who find out, it's already too late. . . .Spanning five decades, from the last days of the 1970s to the present, leaping genres, and barreling toward an astonishing conclusion, this intricately woven novel will pull you into a reality-warping new vision of the haunted house story—as only David Mitchell could imagine it."
    )
    black_chalk = Book(
        title="Black Chalk", 
        author_first_name="Christopher",
        author_last_name="Yates", 
        genre="thriller",
        format="paperback",
        isbn="9781250075550",
        price=18.00,
        front_image="https://m.media-amazon.com/images/I/91dfjOR2zVL._SL1500_.jpg",
        back_image="https://m.media-amazon.com/images/I/81utRGmr5+L._SL1500_.jpg",
        publisher="Picador",
        publication_date="2015-08-04",
        on_hand=10,
        description="It was only ever meant to be a game played by six best friends in their first year at Oxford University; a game of consequences, silly forfeits, and childish dares. But then the game changed: The stakes grew higher and the dares more personal and more humiliating, finally evolving into a vicious struggle with unpredictable and tragic results. Now, fourteen years later, the remaining players must meet again for the final round. Who knows better than your best friends what would break you? A gripping psychological thriller partly inspired by the author's own time at Oxford University, Black Chalk is perfect for fans of the high tension and expert pacing of The Secret History and The Bellwether Revivals. Christopher J. Yates' background in puzzle writing and setting can clearly be seen in the plotting of this clever, tricky book that will keep you guessing to the very end."
    )
    the_picture_of_dorian_gray = Book(
        title="The Picture of Dorian Gray", 
        author_first_name="Oscar",
        author_last_name="Wilde", 
        genre="horror",
        format="paperback",
        isbn="9781435159587",
        price=15.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781435159587_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Barnes and Noble",
        publication_date="2015-03-27",
        on_hand=10,
        description="It was only ever meant to be a game played by six best friends in their first year at Oxford University; a game of consequences, silly forfeits, and childish dares. But then the game changed: The stakes grew higher and the dares more personal and more humiliating, finally evolving into a vicious struggle with unpredictable and tragic results. Now, fourteen years later, the remaining players must meet again for the final round. Who knows better than your best friends what would break you? A gripping psychological thriller partly inspired by the author's own time at Oxford University, Black Chalk is perfect for fans of the high tension and expert pacing of The Secret History and The Bellwether Revivals. Christopher J. Yates' background in puzzle writing and setting can clearly be seen in the plotting of this clever, tricky book that will keep you guessing to the very end."
    )
    the_metamorphosis = Book(
        title="The Metamorphosis", 
        author_first_name="Franz",
        author_last_name="Kafka", 
        genre="fiction",
        format="paperback",
        isbn="9781557427663",
        price=5.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781557427663_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Wildside Press",
        publication_date="2016-08-03",
        on_hand=10,
        description="The Metamorphosisis a short novel by Franz Kafka, first published in 1915. It is often cited as one of the seminal works of fiction of the 20th century and is widely studied in colleges and universities across the western world. The story begins with a traveling salesman, Gregor Samsa, waking to find himself transformed into an insect."
    )
    in_cold_blood = Book(
        title="In Cold Blood", 
        author_first_name="Truman",
        author_last_name="Capote", 
        genre="true crime",
        format="paperback",
        isbn="9780679745587",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780679745587_p0_v3_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="1994-02-01",
        on_hand=10,
        description="On November 15, 1959, in the small town of Holcomb, Kansas, four members of the Clutter family were savagely murdered by blasts from a shotgun held a few inches from their faces. There was no apparent motive for the crime, and there were almost no clues. In one of the first non-fiction novels ever written, Truman Capote reconstructs the murder and the investigation that led to the capture, trial, and execution of the killers, generating both mesmerizing suspense and astonishing empathy. In Cold Blood is a work that transcends its moment, yielding poignant insights into the nature of American violence."
    )
    bunny = Book(
        title="Bunny", 
        author_first_name="Mona",
        author_last_name="Awad", 
        genre="fiction",
        format="paperback",
        isbn="9780525559757",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780525559757_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2020-06-09",
        on_hand=10,
        description="Samantha Heather Mackey couldn't be more of an outsider in her small, highly selective MFA program at New England's Warren University. A scholarship student who prefers the company of her dark imagination to that of most people, she is utterly repelled by the rest of her fiction writing cohort—a clique of unbearably twee rich girls who call each other 'Bunny,' and seem to move and speak as one.But everything changes when Samantha receives an invitation to the Bunnies' fabled 'Smut Salon,' and finds herself inexplicably drawn to their front door—ditching her only friend, Ava, in the process. As Samantha plunges deeper and deeper into the Bunnies' sinister yet saccharine world, beginning to take part in the ritualistic off-campus 'Workshop' where they conjure their monstrous creations, the edges of reality begin to blur. Soon, her friendships with Ava and the Bunnies will be brought into deadly collision. The spellbinding new novel from one of our most fearless chroniclers of the female experience, Bunny is a down-the-rabbit-hole tale of loneliness and belonging, friendship and desire, and the fantastic and terrible power of the imagination."
    )
    brave_new_world = Book(
        title="Brave New World", 
        author_first_name="Aldous",
        author_last_name="Huxley", 
        genre="fiction",
        format="paperback",
        isbn="9780060850524",
        price=16.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780060850524_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2006-10-17",
        on_hand=10,
        description="Aldous Huxley's profoundly important classic of world literature, Brave New World is a searching vision of an unequal, technologically-advanced future where humans are genetically bred, socially indoctrinated, and pharmaceutically anesthetized to passively uphold an authoritarian ruling order—all at the cost of our freedom, full humanity, and perhaps also our souls. “A genius [who] who spent his life decrying the onward march of the Machine” (The New Yorker), Huxley was a man of incomparable talents: equally an artist, a spiritual seeker, and one of history's keenest observers of human nature and civilization. Brave New World, his masterpiece, has enthralled and terrified millions of readers, and retains its urgent relevance to this day as both a warning to be heeded as we head into tomorrow and as a thought-provoking, satisfying work of literature. Written in the shadow of the rise of fascism during the 1930s, Brave New World likewise speaks to a 21st-century world dominated by mass-entertainment, technology, medicine and pharmaceuticals, the arts of persuasion, and the hidden influence of elites."
    )


    


    db.session.add(haunting_of_hill_house) #1
    db.session.add(frankenstein) #2
    db.session.add(something_wicked_this_way_comes) #3
    db.session.add(slade_house) #4
    db.session.add(black_chalk) #5
    db.session.add(the_picture_of_dorian_gray) #6
    db.session.add(the_metamorphosis) #7
    db.session.add(in_cold_blood) #8
    db.session.add(bunny) #9
    db.session.add(brave_new_world) #10
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
