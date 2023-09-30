from app.models import db, Book, environment, SCHEMA
from sqlalchemy.sql import text

#Adds books to the database
def seed_books():
    haunting_of_hill_house = Book(
        title="The Haunting of Hill House", 
        author_first_name="Shirley",
        author_last_name="Jackson", 
        genre="Horror",
        format="Paperback",
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
        genre="Horror",
        format="Paperback",
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
        genre="Horror",
        format="Paperback",
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
        genre="Horror",
        format="Paperback",
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
        genre="Thriller",
        format="Paperback",
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
        genre="Horror",
        format="Paperback",
        isbn="9781435159587",
        price=15.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781435159587_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Barnes and Noble",
        publication_date="2015-03-27",
        on_hand=10,
        description="Horror hides behind an attractive face in The Picture of Dorian Gray, Oscar Wilde's tale of a notorious Victorian libertine and his life of evil excesses. Though Dorian's hedonistic indulgences leave no blemish on his ageless features, the painted portrait imbued with his soul proves a living catalogue of corruption, revealing in its every new line and lesion the manifold sins he has committed. Desperate to hide the physical evidence of his unregenerate spirit, Dorian will stop at nothing—not even murder—to keep his picture's existence a secret."
    )
    the_metamorphosis = Book(
        title="The Metamorphosis", 
        author_first_name="Franz",
        author_last_name="Kafka", 
        genre="Fiction",
        format="Paperback",
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
        format="Paperback",
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
        format="Paperback",
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
        format="Paperback",
        isbn="9780060850524",
        price=16.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780060850524_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2006-10-17",
        on_hand=10,
        description="Aldous Huxley's profoundly important classic of world literature, Brave New World is a searching vision of an unequal, technologically-advanced future where humans are genetically bred, socially indoctrinated, and pharmaceutically anesthetized to passively uphold an authoritarian ruling order—all at the cost of our freedom, full humanity, and perhaps also our souls. “A genius [who] who spent his life decrying the onward march of the Machine” (The New Yorker), Huxley was a man of incomparable talents: equally an artist, a spiritual seeker, and one of history's keenest observers of human nature and civilization. Brave New World, his masterpiece, has enthralled and terrified millions of readers, and retains its urgent relevance to this day as both a warning to be heeded as we head into tomorrow and as a thought-provoking, satisfying work of literature. Written in the shadow of the rise of fascism during the 1930s, Brave New World likewise speaks to a 21st-century world dominated by mass-entertainment, technology, medicine and pharmaceuticals, the arts of persuasion, and the hidden influence of elites."
    )
    wired_that_way = Book(
        title="Wired That Way", 
        author_first_name="Maria",
        author_last_name="Littauer", 
        genre="Self-Help",
        format="Paperback",
        isbn="9780800725372",
        price=16.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780800725372_p0_v6_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Baker Publishing Group",
        publication_date="2006-05-08",
        on_hand=10,
        description="Do you want to better understand yourself, maximize your strengths, and improve your relationships? Understanding how we are wired can enrich our lives and our relationships, helping to overcome differences that can seem irreconcilable. Instead of terminating jobs, friendships, or marriage on grounds of incompatibility, it is possible to turn these relationships from dying to growing. For more than 25 years, Marita Littauer, with her mother, Florence Littauer, has helped thousands of men and women with their personal and professional relationships. In Wired That Way, Marita brings together in one book a comprehensive overview of the personality types that speaks to anyone who wants to understand and to be understood."
    )
    start_with_why = Book(
        title="Start With Why", 
        author_first_name="Simon",
        author_last_name="Sinek", 
        genre="Self-Help",
        format="Paperback",
        isbn="9781591846444",
        price=13.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781591846444_p0_v3_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2011-27-27",
        on_hand=15,
        description="Discover the book that is captivating millions on TikTok and that served as the basis for one of the most popular TED Talks of all time—with more than 56 million views and counting. Over a decade ago, Simon Sinek started a movement that inspired millions to demand purpose at work, to ask what was the WHY of their organization. Since then, millions have been touched by the power of his ideas, and these ideas remain as relevant and timely as ever. START WITH WHY asks (and answers) the questions: why are some people and organizations more innovative, more influential, and more profitable than others? Why do some command greater loyalty from customers and employees alike? Even among the successful, why are so few able to repeat their success over and over? People like Martin Luther King Jr., Steve Jobs, and the Wright Brothers had little in common, but they all started with WHY. They realized that people won't truly buy into a product, service, movement, or idea until they understand the WHY behind it. START WITH WHY shows that the leaders who have had the greatest influence in the world all think, act and communicate the same way—and it's the opposite of what everyone else does. Sinek calls this powerful idea The Golden Circle, and it provides a framework upon which organizations can be built, movements can be led, and people can be inspired. And it all starts with WHY."
    )
    tiny_habits = Book(
        title="Tiny Habits: The Small Changes That Change Everything", 
        author_first_name="BJ",
        author_last_name="Fogg", 
        genre="Self-Help",
        format="Paperback",
        isbn="9780358362777",
        price=14.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780358362777_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B300x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2021-01-19",
        on_hand=10,
        description="BJ FOGG is here to change your life—and revolutionize how we think about human behavior. Based on twenty years of research and Fogg’s experience coaching more than 40,000 people, Tiny Habits cracks the code of habit formation. With breakthrough discoveries in every chapter, you'll learn the simplest proven ways to transform your life. Fogg shows you how to feel good about your successes instead of bad about your failures. This proven, step-by-step guide will help you design habits and make them stick through positive emotion and celebrating small successes. Whether you want to lose weight, de-stress, sleep better, or be more productive each day, Tiny Habits makes it easy to achieve—by starting small."
    )
    atomic_habits = Book(
        title="Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones", 
        author_first_name="James",
        author_last_name="Clear", 
        genre="Self-Help",
        format="Hardcover",
        isbn="9780735211292",
        price=24.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780735211292_p0_v20_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2018-10-16",
        on_hand=20,
        description="No matter your goals, Atomic Habits offers a proven framework for improving—every day. James Clear, one of the world's leading experts on habit formation, reveals practical strategies that will teach you exactly how to form good habits, break bad ones, and master the tiny behaviors that lead to remarkable results. If you're having trouble changing your habits, the problem isn't you. The problem is your system. Bad habits repeat themselves again and again not because you don't want to change, but because you have the wrong system for change. You do not rise to the level of your goals. You fall to the level of your systems. Here, you'll get a proven system that can take you to new heights. Clear is known for his ability to distill complex topics into simple behaviors that can be easily applied to daily life and work. Here, he draws on the most proven ideas from biology, psychology, and neuroscience to create an easy-to-understand guide for making good habits inevitable and bad habits impossible. Along the way, readers will be inspired and entertained with true stories from Olympic gold medalists, award-winning artists, business leaders, life-saving physicians, and star comedians who have used the science of small habits to master their craft and vault to the top of their field. Learn how to: make time for new habits (even when life gets crazy); overcome a lack of motivation and willpower; design your environment to make success easier; get back on track when you fall off course; ...and much more. Atomic Habits will reshape the way you think about progress and success, and give you the tools and strategies you need to transform your habits—whether you are a team looking to win a championship, an organization hoping to redefine an industry, or simply an individual who wishes to quit smoking, lose weight, reduce stress, or achieve any other goal."
    )
    the_four_agreements = Book(
        title="The Four Agreements: A Practical Guide to Personal Freedom", 
        author_first_name="don Miguel",
        author_last_name="Ruiz", 
        genre="Self-Help",
        format="Paperback",
        isbn="9781878424310",
        price=12.95,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781878424310_p0_v7_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Amber-Allen Publishing",
        publication_date="1997-11-07",
        on_hand=20,
        description="In The Four Agreements, bestselling author don Miguel Ruiz reveals the source of self-limiting beliefs that rob us of joy and create needless suffering. Based on ancient Toltec wisdom, The Four Agreements offer a powerful code of conduct that can rapidly transform our lives to a new experience of freedom, true happiness, and love."
    )
    on_earth_were_briefly_gorgeous = Book(
        title="On Earth We're Briefly Gorgeous", 
        author_first_name="Ocean",
        author_last_name="Vuong", 
        genre="Fiction",
        format="Paperback",
        isbn="9780525562047",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780525562047_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2021-01-2021",
        on_hand=10,
        description="On Earth We're Briefly Gorgeous is a letter from a son to a mother who cannot read. Written when the speaker, Little Dog, is in his late twenties, the letter unearths a family’s history that began before he was born — a history whose epicenter is rooted in Vietnam — and serves as a doorway into parts of his life his mother has never known, all of it leading to an unforgettable revelation. At once a witness to the fraught yet undeniable love between a single mother and her son, it is also a brutally honest exploration of race, class, and masculinity. Asking questions central to our American moment, immersed as we are in addiction, violence, and trauma, but undergirded by compassion and tenderness, On Earth We’re Briefly Gorgeous is as much about the power of telling one’s own story as it is about the obliterating silence of not being heard. With stunning urgency and grace, Ocean Vuong writes of people caught between disparate worlds, and asks how we heal and rescue one another without forsaking who we are. The question of how to survive, and how to make of it a kind of joy, powers the most important debut novel of many years."
    )
    the_buddha_in_the_attic = Book(
        title="The Buddha in the Attic", 
        author_first_name="Julie",
        author_last_name="Otsuka", 
        genre="Fiction",
        format="Paperback",
        isbn="9780307744425",
        price=16.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780307744425_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="2012-03-20",
        on_hand=10,
        description="In eight unforgettable sections, The Buddha in the Attic traces the extraordinary lives of these women, from their arduous journeys by boat, to their arrival in San Francisco and their tremulous first nights as new wives; from their experiences raising children who would later reject their culture and language, to the deracinating arrival of war. Julie Otsuka has written a spellbinding novel about identity and loyalty, and what it means to be an American in uncertain times."
    )
    fight_club = Book(
        title="Fight Club: A Novel", 
        author_first_name="Chuck",
        author_last_name="Palahniuk", 
        genre="Fiction",
        format="Paperback",
        isbn="9780393355949",
        price=15.95,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780393355949_p0_v7_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Norton, W. W. & Company, Inc.",
        publication_date="2018-05-01",
        on_hand=10,
        description="We understand that the first rule of Fight Club is to not talk about Fight Club, but it’s too good not to talk about. If ever there was a book that defined Chuck Palahniuk in all of his unhinged brilliance, this is it. A gritty, grimy, oft-disturbing story that still manages to effectively explore mental health and masculinity. The first rule about fight club is you don't talk about fight club. Chuck Palahniuk showed himself to be his generation's most visionary satirist in this, his first book. Fight Club's estranged narrator leaves his lackluster job when he comes under the thrall of Tyler Durden, an enigmatic young man who holds secret after-hours boxing matches in the basements of bars. There, two men fight 'as long as they have to.' This is a gloriously original work that exposes the darkness at the core of our modern world."
    )
    the_burning_girls = Book(
        title="The Burning Girls", 
        author_first_name="C.J.",
        author_last_name="Tudor", 
        genre="Horror",
        format="Paperback",
        isbn="9781984825049",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781984825049_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Random House Publishing Group",
        publication_date="2022-01-04",
        on_hand=15,
        description="A dark history lingers in Chapel Croft. Five hundred years ago, local Protestant martyrs were betrayed—then burned. Thirty years ago, two teenage girls disappeared without a trace. And a few weeks ago, the vicar of the local parish hanged himself in the nave of the church. Reverend Jack Brooks, a single parent with a fourteen-year-old daughter and a heavy conscience, arrives in the village hoping for a fresh start. Instead, Jack finds a town rife with conspiracies and secrets, and is greeted with a strange welcome package: an exorcism kit and a note that warns, “But there is nothing covered up that will not be revealed and hidden that will not be known.” The more Jack and daughter, Flo, explore the town and get to know its strange denizens, the deeper they are drawn into the age-old rifts, mysteries, and suspicions. And when Flo begins to see specters of girls ablaze, it becomes apparent there are ghosts here that refuse to be laid to rest. Uncovering the truth can be deadly in a village with a bloody past, where everyone has something to hide and no one trusts an outsider."
    )
    house_of_leaves = Book(
        title="House of Leaves: The Remastered Full-Color Edition", 
        author_first_name="Mark Z.",
        author_last_name="Danielewski", 
        genre="Horror",
        format="Paperback",
        isbn="9780375703768",
        price=29.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780375703768_p0_v7_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="2000-03-07",
        on_hand=13,
        description="Years ago, when House of Leaves was first being passed around, it was nothing more than a badly bundled heap of paper, parts of which would occasionally surface on the Internet. No one could have anticipated the small but devoted following this terrifying story would soon command. Starting with an odd assortment of marginalized youth—musicians, tattoo artists, programmers, strippers, environmentalists, and adrenaline junkies—the book eventually made its way into the hands of older generations, who not only found themselves in those strangely arranged pages but also discovered a way back into the lives of their estranged children. Now made available in book form, complete with the original colored words, vertical footnotes, and second and third appendices, the story remains unchanged. Similarly, the cultural fascination with House of Leaves remains as fervent and as imaginative as ever. The novel has gone on to inspire doctorate-level courses and masters theses, cultural phenomena like the online urban legend of “the backrooms,” and incredible works of art in entirely unrealted mediums from music to video games. Neither Pulitzer Prize-winning photojournalist Will Navidson nor his companion Karen Green was prepared to face the consequences of the impossibility of their new home, until the day their two little children wandered off and their voices eerily began to return another story—of creature darkness, of an ever-growing abyss behind a closet door, and of that unholy growl which soon enough would tear through their walls and consume all their dreams."
    )
    the_secret_history = Book(
        title="The Secret History", 
        author_first_name="Donna",
        author_last_name="Tartt", 
        genre="Fiction",
        format="Paperback",
        isbn="9781400031702",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781400031702_p0_v10_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="2004-04-13",
        on_hand=15,
        description="Under the influence of a charismatic classics professor, a group of clever, eccentric misfits at a New England college discover a way of thought and life a world away from their banal contemporaries. But their search for the transcendent leads them down a dangerous path, beyond human constructs of morality."
    )
    the_midnight_library = Book(
        title="The Midnight Library", 
        author_first_name="Matt",
        author_last_name="Haig", 
        genre="Fiction",
        format="Paperback",
        isbn="9780525559498",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780525559498_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2023-05-09",
        on_hand=15,
        description="Somewhere out beyond the edge of the universe there is a library that contains an infinite number of books, each one the story of another reality. One tells the story of your life as it is, along with another book for the other life you could have lived if you had made a different choice at any point in your life. While we all wonder how our lives might have been, what if you had the chance to go to the library and see for yourself? Would any of these other lives truly be better? In The Midnight Library, Matt Haig's enchanting blockbuster novel, Nora Seed finds herself faced with this decision. Faced with the possibility of changing her life for a new one, following a different career, undoing old breakups, realizing her dreams of becoming a glaciologist; she must search within herself as she travels through the Midnight Library to decide what is truly fulfilling in life, and what makes it worth living in the first place."
    )
    firekeepers_daughter = Book(
        title="Firekeeper's Daughter", 
        author_first_name="Angeline",
        author_last_name="Boulley", 
        genre="Fiction",
        format="Paperback",
        isbn="9781250766564",
        price=19.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781250766564_p0_v11_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Henry Holt and Co. (BYR)",
        publication_date="2021-03-16",
        on_hand=15,
        description="Eighteen-year-old Daunis Fontaine has never quite fit in, both in her hometown and on the nearby Ojibwe reservation. She dreams of a fresh start at college, but when family tragedy strikes, Daunis puts her future on hold to look after her fragile mother. The only bright spot is meeting Jamie, the charming new recruit on her brother Levi’s hockey team. Yet even as Daunis falls for Jamie, she senses the dashing hockey star is hiding something. Everything comes to light when Daunis witnesses a shocking murder, thrusting her into an FBI investigation of a lethal new drug. Reluctantly, Daunis agrees to go undercover, drawing on her knowledge of chemistry and Ojibwe traditional medicine to track down the source. But the search for truth is more complicated than Daunis imagined, exposing secrets and old scars. At the same time, she grows concerned with an investigation that seems more focused on punishing the offenders than protecting the victims. Now, as the deceptions—and deaths—keep growing, Daunis must learn what it means to be a strong Anishinaabe kwe (Ojibwe woman) and how far she’ll go for her community, even if it tears apart the only world she’s ever known."
    )
    where_the_crawdads_sing = Book(
        title="Where the Crawdads Sing", 
        author_first_name="Delia",
        author_last_name="Owens", 
        genre="Fiction",
        format="Paperback",
        isbn="9780735219106",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780735219106_p0_v11_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2021-03-30",
        on_hand=15,
        description="For years, rumors of the “Marsh Girl” have haunted Barkley Cove, a quiet town on the North Carolina coast. So in late 1969, when handsome Chase Andrews is found dead, the locals immediately suspect Kya Clark, the so-called Marsh Girl. But Kya is not what they say. Sensitive and intelligent, she has survived for years alone in the marsh that she calls home, finding friends in the gulls and lessons in the sand. Then the time comes when she yearns to be touched and loved. When two young men from town become intrigued by her wild beauty, Kya opens herself to a new life—until the unthinkable happens. Where the Crawdads Sing is at once an exquisite ode to the natural world, a heartbreaking coming-of-age story, and a surprising tale of possible murder. Owens reminds us that we are forever shaped by the children we once were, and that we are all subject to the beautiful and violent secrets that nature keeps."
    )
    stardust = Book(
        title="Stardust", 
        author_first_name="Neil",
        author_last_name="Gaiman", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780061689246",
        price=15.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780061689246_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2008-12-23",
        on_hand=15,
        description="Catch a fallen star . . . Tristran Thorn promised to bring back a fallen star. So he sets out on a journey to fulfill the request of his beloved, the hauntingly beautiful Victoria Forester—and stumbles into the enchanted realm that lies beyond the wall of his English country town. Rich with adventure and magic, Stardust is one of master storyteller Neil Gaiman's most beloved tales, and the inspiration for the hit movie."
    )
    in_a_dark_dark_wood = Book(
        title="In a Dark, Dark Wood", 
        author_first_name="Ruth",
        author_last_name="Ware", 
        genre="Thriller",
        format="Paperback",
        isbn="	9781501112331",
        price=17.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781501112331_p0_v7_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B300x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Gallery/Scout Press",
        publication_date="2016-04-19",
        on_hand=10,
        description="When reclusive writer Leonora is invited to the English countryside for a weekend away, she reluctantly agrees to make the trip. But as the first night falls, revelations unfold among friends old and new, an unnerving memory shatters Leonora’s reserve, and a haunting realization creeps in: the party is not alone in the woods."
    )
    the_goldfinch = Book(
        title="The Goldfinch", 
        author_first_name="Donna",
        author_last_name="Tartt", 
        genre="Fiction",
        format="Paperback",
        isbn="9780316055444",
        price=20.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780316055444_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Little, Brown and Company",
        publication_date="2015-04-07",
        on_hand=10,
        description="Theo Decker, a 13-year-old New Yorker, miraculously survives an accident that kills his mother. Abandoned by his father, Theo is taken in by the family of a wealthy friend. Bewildered by his strange new home on Park Avenue, disturbed by schoolmates who don't know how to talk to him, and tormented above all by a longing for his mother, he clings to the one thing that reminds him of her: a small, mysteriously captivating painting that ultimately draws Theo into a wealthy and insular art community. As an adult, Theo moves silkily between the drawing rooms of the rich and the dusty labyrinth of an antiques store where he works. He is alienated and in love — and at the center of a narrowing, ever more dangerous circle. The Goldfinch is a mesmerizing, stay-up-all-night and tell-all-your-friends triumph, an old-fashioned story of loss and obsession, survival and self-invention. From the streets of New York to the dark corners of the art underworld, this 'soaring masterpiece' examines the devastating impact of grief and the ruthless machinations of fate (Ron Charles, Washington Post)."
    )
    the_little_friend = Book(
        title="The Little Friend", 
        author_first_name="Donna",
        author_last_name="Tartt", 
        genre="Fiction",
        format="Paperback",
        isbn="9781400031696",
        price=19.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781400031696_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="2003-10-28",
        on_hand=10,
        description="The setting is Alexandria, Mississippi, where one Mother’s Day a little boy named Robin Cleve Dufresnes was found hanging from a tree in his parents’ yard. Twelve years later Robin’s murder is still unsolved and his family remains devastated. So it is that Robin’s sister Harriet—unnervingly bright, insufferably determined, and unduly influenced by the fiction of Kipling and Robert Louis Stevenson—sets out to unmask his killer. Aided only by her worshipful friend Hely, Harriet crosses her town’s rigid lines of race and caste and burrows deep into her family’s history of loss. Filled with hairpin turns of plot and “a bustling, ridiculous humanity worthy of Dickens” (The New York Times Book Review), The Little Friend is a work of myriad enchantments by a writer of prodigious talent."
    )
    fahrenheit_451= Book(
        title="Fahrenheit 451", 
        author_first_name="Ray",
        author_last_name="Bradbury", 
        genre="Science Fiction",
        format="Paperback",
        isbn="9781451673319",
        price=17.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781451673319_p0_v11_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Simon & Schuster",
        publication_date="2012-01-10",
        on_hand=10,
        description="Ray Bradbury's internationally acclaimed novel Fahrenheit 451 is a masterwork of twentieth-century literature set in a bleak, dystopian future. Guy Montag is a fireman. In his world, where television rules and literature is on the brink of extinction, firemen start fires rather than put them out. His job is to destroy the most illegal of commodities, the printed book, along with the houses in which they are hidden. Montag never questions the destruction and ruin his actions produce, returning each day to his bland life and wife, Mildred, who spends all day with her television “family.” But then he meets an eccentric young neighbor, Clarisse, who introduces him to a past where people didn’t live in fear and to a present where one sees the world through the ideas in books instead of the mindless chatter of television. When Mildred attempts suicide and Clarisse suddenly disappears, Montag begins to question everything he has ever known. He starts hiding books in his home, and when his pilfering is discovered, the fireman has to run for his life."
    )
    catcher_in_the_rye= Book(
        title="The Catcher in the Rye", 
        author_first_name="J.D.",
        author_last_name="Salinger", 
        genre="Fiction",
        format="Paperback",
        isbn="9780316769174",
        price=16.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780316769174_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Little, Brown and Company",
        publication_date="2001-01-30",
        on_hand=10,
        description="The hero-narrator of The Catcher in the Rye is an ancient child of sixteen, a native New Yorker named Holden Caufield. Through circumstances that tend to preclude adult, secondhand description, he leaves his prep school in Pennsylvania and goes underground in New York City for three days."
    )
    the_ex_hex= Book(
        title="The Ex Hex: A Novel", 
        author_first_name="Erin",
        author_last_name="Sterling", 
        genre="Romance",
        format="Paperback",
        isbn="9780063027473",
        price=16.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780063027473_p0_v8_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2021-09-28",
        on_hand=10,
        description="Nine years ago, Vivienne Jones nursed her broken heart like any young witch would: vodka, weepy music, bubble baths…and a curse on the horrible boyfriend. Sure, Vivi knows she shouldn’t use her magic this way, but with only an “orchard hayride” scented candle on hand, she isn't worried it will cause him anything more than a bad hair day or two. That is until Rhys Penhallow, descendent of the town's ancestors, breaker of hearts, and annoyingly just as gorgeous as he always was, returns to Graves Glen, Georgia. What should be a quick trip to recharge the town's ley lines and make an appearance at the annual fall festival turns disastrously wrong. With one calamity after another striking Rhys, Vivi realizes her silly little Ex Hex may not have been so harmless after all. Suddenly, Graves Glen is under attack from murderous wind-up toys, a pissed off ghost, and a talking cat with some interesting things to say. Vivi and Rhys have to ignore their off the charts chemistry to work together to save the town and find a way to break the break-up curse before it's too late."
    )
    hollywood_wives= Book(
        title="Hollywood Wives", 
        author_first_name="Jackie",
        author_last_name="Collins", 
        genre="Romance",
        format="Paperback",
        isbn="9781668015384",
        price=19.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781668015384_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B300x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Gallery Books",
        publication_date="2023-07-11",
        on_hand=10,
        description="They're a privileged breed—glamorous, glossy, and demanding. When life is this fast, there are no guarantees. Status is everything, and you're only ever as popular as your husband's latest box-office hit. Elaine Conti: Bronx girl turned Hollywood hostess, determined to relaunch her husband's fading acting career back into orbit. Angel Hudson: Married to a hot young actor and an innocent beauty prey to Hollywood's most unscrupulous men. Montana Grey: Gorgeous renegade, ambitiously driven to succeed in the male-dominated world on the other side of the camera. Hollywood Wives is a scorching blockbuster that exposes the glittering microcosm that is Beverly Hills before racing to a gripping and unexpected climax. Captivating, fun, and deliciously sexy, this classic is its own version of Hollywood magic."
    )
    valley_of_the_dolls= Book(
        title="Valley of the Dolls", 
        author_first_name="Jacqueline",
        author_last_name="Susann", 
        genre="Romance",
        format="Paperback",
        isbn="9780802125347",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780802125347_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Grove/Atlantic, Inc.",
        publication_date="2016-07-14",
        on_hand=10,
        description="At a time when women were destined to become housewives, Jacqueline Susann let us dream. Anne, Neely, and Jennifer become best friends as struggling young women in New York City trying to make their mark. Eventually, they climb their way to the top of the entertainment industry only to find that there’s no place left to go but down, into the Valley of the Dolls."
    )
    anna_karenina= Book(
        title="Anna Karenina", 
        author_first_name="Leo",
        author_last_name="Tolstoy", 
        genre="Romance",
        format="Paperback",
        isbn="9781562170332",
        price=29.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781562170332_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Heffner Publishing",
        publication_date="2022-01-12",
        on_hand=10,
        description="Anna Karenina chronicles the doomed love affair between Anna and the dashing Count Vronsky. Married to a much older man, tragedy unfolds when Anna risks all in pursuit a more passionate and fulfilling life. Often described as one of the greatest novels ever written."
    )
    the_omnivores_dilemma= Book(
        title="The Omnivore's Dilemma: A Natural History of Four Meals", 
        author_first_name="Michael",
        author_last_name="Pollan", 
        genre="Nonfiction",
        format="Paperback",
        isbn="9780143038580",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780143038580_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Publishing Group",
        publication_date="2007-08-28",
        on_hand=10,
        description="What should we have for dinner? Ten years ago, Michael Pollan confronted us with this seemingly simple question and, with The Omnivore’s Dilemma, his brilliant and eye-opening exploration of our food choices, demonstrated that how we answer it today may determine not only our health but our survival as a species. In the years since, Pollan’s revolutionary examination has changed the way Americans think about food. Bringing wide attention to the little-known but vitally important dimensions of food and agriculture in America, Pollan launched a national conversation about what we eat and the profound consequences that even the simplest everyday food choices have on both ourselves and the natural world. Ten years later, The Omnivore’s Dilemma continues to transform the way Americans think about the politics, perils, and pleasures of eating."
    )
    the_billionaires_vinegar= Book(
        title="The Billionaire's Vinegar: The Mystery of the World's Most Expensive Bottle of Wine", 
        author_first_name="Benjamin",
        author_last_name="Wallace", 
        genre="Nonfiction",
        format="Paperback",
        isbn="9780307338785",
        price=18.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780307338785_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Crown Publishing Group",
        publication_date="2009-04-14",
        on_hand=10,
        description="The New York Times bestseller, updated with a new epilogue, that tells the true story of a 1787 Château Lafite Bordeaux—supposedly owned by Thomas Jefferson—that sold for $156,000 at auction and of the eccentrics whose lives intersected with it. Was it truly entombed in a Paris cellar for two hundred years? Or did it come from a secret Nazi bunker? Or from the moldy basement of a devilishly brilliant con artist? As Benjamin Wallace unravels the mystery, we meet a gallery of intriguing players—from the bicycle-riding British auctioneer who speaks of wines as if they are women to the obsessive wine collector who discovered the bottle. Suspenseful and thrillingly strange, this is the vintage tale of what could be the most elaborate con since the Hitler diaries."
    )
    the_big_burn= Book(
        title="The Big Burn: Teddy Roosevelt and the Fire that Saved America", 
        author_first_name="Timothy",
        author_last_name="Egan", 
        genre="Nonfiction",
        format="Paperback",
        isbn="9780547394602",
        price=17.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780547394602_p0_v7_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2010-09-07",
        on_hand=10,
        description="A dramatic account of the worst forest fire in American history by the author of the National Book Award–winning The Worst Hard Time. On the afternoon of August 20, 1910, a battering ram of wind moved through the drought-stricken national forest of Washington, Idaho, and Montana, whipping the hundreds of small blazes burning across the forest floor into a roaring inferno. Forest rangers had assembled nearly ten thousand men—college boys, day workers, immigrants from mining camps—to fight the fire. But no living person had seen anything like those flames, and neither the rangers nor anyone else knew how to subdue them. Timothy Egan narrates the struggles of the overmatched ranges against the implacable fire with unstoppable dramatic force. Equally dramatic is the larger story he tells of outsize president Teddy Roosevelt ad his chief forester, Gifford Pinchot. Pioneering the notion of conservation, Roosevelt and Pinchot did nothing less than create the idea of public land as our national treasure, owned by and preserved for every citizen."
    )
    the_yosemite= Book(
        title="The Yosemite", 
        author_first_name="John",
        author_last_name="Muir", 
        genre="Nonfiction",
        format="Paperback",
        isbn="9780486825557",
        price=14.95,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780486825557_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B300x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Dover Publications",
        publication_date="2018-09-12",
        on_hand=10,
        description="An essential companion for visitors, this book by the famed conservationist offers informed appraisals of Yosemite's plant and animal life and exudes an almost mystical love for its natural beauty."
    )
    the_art_thief= Book(
        title="The Art Thief: A True Story of Love, Crime, and a Dangerous Obsession", 
        author_first_name="Michael",
        author_last_name="Finkel", 
        genre="Nonfiction",
        format="Hardcover",
        isbn="9780525657323",
        price=28.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780525657323_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Knopf Doubleday Publishing Group",
        publication_date="2023-06-27",
        on_hand=10,
        description="In this spellbinding portrait of obsession and flawed genius, the best-selling author of The Stranger in the Woods brings us into Breitwieser’s strange world—unlike most thieves, he never stole for money, keeping all his treasures in a single room where he could admire them. For centuries, works of art have been stolen in countless ways from all over the world, but no one has been quite as successful at it as the master thief Stéphane Breitwieser. Carrying out more than two hundred heists over nearly eight years—in museums and cathedrals all over Europe—Breitwieser, along with his girlfriend who worked as his lookout, stole more than three hundred objects, until it all fell apart in spectacular fashion. In The Art Thief, Michael Finkel brings us into Breitwieser's strange and fascinating world. Unlike most thieves, Breitwieser never stole for money. Instead, he displayed all his treasures in a pair of secret rooms where he could admire them to his heart's content. Possessed of a remarkable athleticism and an innate ability to circumvent practically any security system, Breitwieser managed to pull off a breathtaking number of audacious thefts. Yet these strange talents bred a growing disregard for risk and an addict’s need to score, leading Breitwieser to ignore his girlfriend’s pleas to stop—until one final act of hubris brought everything crashing down. This is a riveting story of art, crime, love, and an insatiable hunger to possess beauty at any cost."
    )
    a_house_in_the_sky= Book(
        title="A House in the Sky: A Memoir", 
        author_first_name="Amanda",
        author_last_name="Lindhout", 
        genre="Autobiography",
        format="Paperback",
        isbn="9781451645613",
        price=19.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780525657323_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scribner",
        publication_date="2014-06-17",
        on_hand=10,
        description="As a child, Amanda Lindhout escaped a violent household by paging through issues of National Geographic and imagining herself visiting its exotic locales. At the age of nineteen, working as a cocktail waitress, she began saving her tips so she could travel the globe. Aspiring to understand the world and live a significant life, she backpacked through Latin America, Laos, Bangladesh, and India, and emboldened by each adventure, went on to Sudan, Syria, and Pakistan. In war-ridden Afghanistan and Iraq she carved out a fledgling career as a television reporter. And then, in August 2008, she traveled to Somalia—“the most dangerous place on earth.” On her fourth day, she was abducted by a group of masked men along a dusty road. Held hostage for 460 days, Amanda survives on memory—every lush detail of the world she experienced in her life before captivity—and on strategy, fortitude, and hope. When she is most desperate, she visits a house in the sky, high above the woman kept in chains, in the dark. Vivid and suspenseful, as artfully written as the finest novel, A House in the Sky is “a searingly unsentimental account. Ultimately it is compassion—for her naïve younger self, for her kidnappers—that becomes the key to Lindhout's survival” (O, The Oprah Magazine)."
    )
    educated = Book(
        title="Educated: A Memoir", 
        author_first_name="Tara",
        author_last_name="Westover", 
        genre="Autobiography",
        format="Paperback",
        isbn="9780399590528",
        price=18.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780399590528_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Random House Publishing Group",
        publication_date="2022-02-08",
        on_hand=10,
        description="Born to survivalists in the mountains of Idaho, Tara Westover was seventeen the first time she set foot in a classroom. Her family was so isolated from mainstream society that there was no one to ensure the children received an education, and no one to intervene when one of Tara’s older brothers became violent. When another brother got himself into college, Tara decided to try a new kind of life. Her quest for knowledge transformed her, taking her over oceans and across continents, to Harvard and to Cambridge University. Only then would she wonder if she’d traveled too far, if there was still a way home."
    )
    the_glass_castle = Book(
        title="The Glass Castle", 
        author_first_name="Jeannette",
        author_last_name="Walls", 
        genre="Autobiography",
        format="Paperback",
        isbn="9780743247542",
        price=17.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780743247542_p0_v12_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&product=path%5B/pimages/9780743247542_p2_v1%5D&call=url%5Bfile:common/decodeProduct.chain%5D",
        publisher="Scribner",
        publication_date="2006-01-17",
        on_hand=10,
        description="The Glass Castle is a remarkable memoir of resilience and redemption, and a revelatory look into a family at once deeply dysfunctional and uniquely vibrant. When sober, Jeannette’s brilliant and charismatic father captured his children’s imagination, teaching them physics, geology, and how to embrace life fearlessly. But when he drank, he was dishonest and destructive. Her mother was a free spirit who abhorred the idea of domesticity and didn't want the responsibility of raising a family. The Walls children learned to take care of themselves. They fed, clothed, and protected one another, and eventually found their way to New York. Their parents followed them, choosing to be homeless even as their children prospered. The Glass Castle is truly astonishing—a memoir permeated by the intense love of a peculiar but loyal family."
    )
    making_it_so = Book(
        title="Making It So: A Memoir", 
        author_first_name="Patrick",
        author_last_name="Stewart", 
        genre="Autobiography",
        format="Hardcover",
        isbn="9781982167738",
        price=35.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781982167738_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Gallery Books",
        publication_date="2023-10-03",
        on_hand=10,
        description="The riveting memoir of the indelible Sir Patrick Stewart, from his days on stage to his iconic roles as Captain Picard and Professor Charles Xavier. He has brought life to countless characters, but this is the story of who he truly is. The long-awaited memoir from iconic, beloved actor and living legend Sir Patrick Stewart! From his acclaimed stage triumphs to his legendary onscreen work in the Star Trek and X-Men franchises, Sir Patrick Stewart has captivated audiences around the world and across multiple generations with his indelible command of stage and screen. Now, he presents his long-awaited memoir, Making It So, a revealing portrait of an artist whose astonishing life—from his humble beginnings in Yorkshire, England, to the heights of Hollywood and worldwide acclaim—proves a story as exuberant, definitive, and enduring as the author himself."
    )
    i_am_not_your_perfect_mexican_daughter = Book(
        title="I Am Not Your Perfect Mexican Daughter", 
        author_first_name="Erika L.",
        author_last_name="Sánchez", 
        genre="Young Adult",
        format="Hardcover",
        isbn="9781524700485",
        price=19.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781524700485_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Random House Children's Books",
        publication_date="2017-10-17",
        on_hand=10,
        description="Perfect Mexican daughters do not go away to college. And they do not move out of their parents’ house after high school graduation. Perfect Mexican daughters never abandon their family. But Julia is not your perfect Mexican daughter. That was Olga's role. Then a tragic accident on the busiest street in Chicago leaves Olga dead and Julia left behind to reassemble the shattered pieces of her family. And no one seems to acknowledge that Julia is broken, too. Instead, her mother seems to channel her grief into pointing out every possible way Julia has failed. But it's not long before Julia discovers that Olga might not have been as perfect as everyone thought. With the help of her best friend Lorena, and her first love, first everything boyfriend Connor, Julia is determined to find out. Was Olga really what she seemed? Or was there more to her sister's story? And either way, how can Julia even attempt to live up to a seemingly impossible ideal?"
    )
    the_fault_in_our_stars = Book(
        title="The Fault in Our Stars", 
        author_first_name="John",
        author_last_name="Green", 
        genre="Young Adult",
        format="Paperback",
        isbn="9780142424179",
        price=14.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780142424179_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Young Readers Group",
        publication_date="2014-04-08",
        on_hand=10,
        description="Despite the tumor-shrinking medical miracle that has bought her a few years, Hazel has never been anything but terminal, her final chapter inscribed upon diagnosis. But when a gorgeous plot twist named Augustus Waters suddenly appears at Cancer Kid Support Group, Hazel's story is about to be completely rewritten. From John Green, #1 bestselling author of The Anthropocene Reviewed and Turtles All the Way Down, The Fault in Our Stars is insightful, bold, irreverent, and raw. It brilliantly explores the funny, thrilling, and tragic business of being alive and in love."
    )
    looking_for_alaska = Book(
        title="Looking For Alaska", 
        author_first_name="John",
        author_last_name="Green", 
        genre="Young Adult",
        format="Paperback",
        isbn="9780142402511",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780142402511_p0_v6_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Penguin Young Readers Group",
        publication_date="2006-12-28",
        on_hand=10,
        description="First drink. First prank. First friend. First love. Last words. Miles Halter is fascinated by famous last words—and tired of his safe life at home. He leaves for boarding school to seek what the dying poet François Rabelais called the “Great Perhaps.” Much awaits Miles at Culver Creek, including Alaska Young, who will pull Miles into her labyrinth and catapult him into the Great Perhaps. Looking for Alaska brilliantly chronicles the indelible impact one life can have on another. A modern classic, this stunning debut marked #1 bestselling author John Green’s arrival as a groundbreaking new voice in contemporary fiction."
    )
    uglies = Book(
        title="Uglies", 
        author_first_name="Scott",
        author_last_name="Westerfield", 
        genre="Young Adult",
        format="Paperback",
        isbn="9781442419810",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781442419810_p0_v11_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781442419810_p2_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        publisher="Simon & Schuster Books For Young Readers",
        publication_date="2011-05-03",
        on_hand=10,
        description="Tally is about to turn sixteen, and she can't wait. In just a few weeks she'll have the operation that will turn her from a repellent ugly into a stunningly attractive pretty. And as a pretty, she'll be catapulted into a high-tech paradise where her only job is to have fun. But Tally's new friend Shay isn't sure she wants to become a pretty. When Shay runs away, Tally learns about a whole new side of the pretty world—and it isn't very pretty. The authorities offer Tally a choice: find her friend and turn her in, or never turn pretty at all. Tally's choice will change her world forever."
    )
    the_giver = Book(
        title="The Giver", 
        author_first_name="Lois",
        author_last_name="Lowry", 
        genre="Young Adult",
        format="Paperback",
        isbn="9780544336261",
        price=11.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780544336261_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2014-07-01",
        on_hand=10,
        description="Life in the community where Jonas lives is idyllic. Designated birthmothers produce newchildren, who are assigned to appropriate family units. Citizens are assigned their partners and their jobs. No one thinks to ask questions. Everyone obeys. Everyone is the same. Except Jonas. Not until he is given his life assignment as the Receiver of Memory does he begin to understand the dark, complex secrets behind his fragile community. Gradually Jonas learns that power lies in feelings. But when his own power is put to the test—when he must try to save someone he loves—he may not be ready. Is it too soon? Or too late? Told with deceptive simplicity, this is the provocative story of a boy who experiences something incredible and undertakes something impossible. In the telling it questions every value we have taken for granted and reexamines our most deeply held beliefs."
    )
    the_martian = Book(
        title="The Martian", 
        author_first_name="Andy",
        author_last_name="Weir", 
        genre="Science Fiction",
        format="Paperback",
        isbn="9780553418026",
        price=17.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780553418026_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Random House Publishing Group",
        publication_date="2014-10-28",
        on_hand=10,
        description="After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead, Mark finds himself stranded and completely alone with no way to even signal Earth that he’s alive—and even if he could get word out, his supplies would be gone long before a rescue could arrive. Chances are, though, he won't have time to starve to death. The damaged machinery, unforgiving environment, or plain-old 'human error' are much more likely to kill him first. But Mark isn't ready to give up yet. Drawing on his ingenuity, his engineering skills—and a relentless, dogged refusal to quit—he steadfastly confronts one seemingly insurmountable obstacle after the next. Will his resourcefulness be enough to overcome the impossible odds against him?"
    )
    do_androids_dream_of_electric_sheep = Book(
        title="Do Androids Dream of Electric Sheep?", 
        author_first_name="Philip K.",
        author_last_name="Dick", 
        genre="Science Fiction",
        format="Paperback",
        isbn="9780345404473",
        price=17.00,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780345404473_p0_v6_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Random House Worlds",
        publication_date="1996-05-28",
        on_hand=10,
        description="By 2021, the World War has killed millions, driving entire species into extinction and sending mankind off-planet. Those who remain covet any living creature, and for people who can’t afford one, companies built incredibly realistic simulacra: horses, birds, cats, sheep. They’ve even built humans. Immigrants to Mars receive androids so sophisticated they are indistinguishable from true men or women. Fearful of the havoc these artificial humans can wreak, the government bans them from Earth. Driven into hiding, unauthorized androids live among human beings, undetected. Rick Deckard, an officially sanctioned bounty hunter, is commissioned to find rogue androids and “retire” them. But when cornered, androids fight back—with lethal force."
    )
    the_hobbit = Book(
        title="The Hobbit", 
        author_first_name="J. R. R.",
        author_last_name="Tolkien", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780547928227",
        price=17.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780547928227_p0_v3_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="HarperCollins Publishers",
        publication_date="2012-09-18",
        on_hand=10,
        description="Bilbo Baggins is a hobbit who enjoys a comfortable, unambitious life, rarely traveling any farther than his pantry or cellar. But his contentment is disturbed when the wizard Gandalf and a company of dwarves arrive on his doorstep one day to whisk him away on an adventure. They have launched a plot to raid the treasure hoard guarded by Smaug the Magnificent, a large and very dangerous dragon. Bilbo reluctantly joins their quest, unaware that on his journey to the Lonely Mountain he will encounter both a magic ring and a frightening creature known as Gollum. Written for J.R.R. Tolkien's own children, The Hobbit has sold many millions of copies worldwide and established itself as a modern classic."
    )
    harry_potter_and_the_sorcerers_stone = Book(
        title="Harry Potter and the Sorcerer's Stone", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9781338878929",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781338878929_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2023-05-02",
        on_hand=10,
        description="Harry Potter has never been the star of a Quidditch team, scoring points while riding a broom far above the ground. He knows no spells, has never helped to hatch a dragon, and has never worn a cloak of invisibility. All he knows is a miserable life with the Dursleys, his horrible aunt and uncle, and their abominable son, Dudley - a great big swollen spoiled bully. Harry's room is a tiny closet at the foot of the stairs, and he hasn't had a birthday party in eleven years. But all that is about to change when a mysterious letter arrives by owl messenger: a letter with an invitation to an incredible place that Harry - and anyone who reads about him - will find unforgettable."
    )
    harry_potter_and_the_chamber_of_secrets = Book(
        title="Harry Potter and the Chamber of Secrets", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9781338878936",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781338878936_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2023-05-02",
        on_hand=10,
        description="The Dursleys were so mean and hideous that summer that all Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he's packing his bags, Harry receives a warning from a strange, impish creature named Dobby who says that if Harry Potter returns to Hogwarts, disaster will strike. And strike it does. For in Harry's second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor, Gilderoy Lockhart, a spirit named Moaning Myrtle who haunts the girls' bathroom, and the unwanted attentions of Ron Weasley's younger sister, Ginny."
    )
    harry_potter_and_the_prisoner_of_azkaban = Book(
        title="Harry Potter and the Prisoner of Azkaban", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780439136358",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781338878943_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="1999-10-01",
        on_hand=10,
        description="For twelve long years, the dread fortress of Azkaban held an infamous prisoner named Sirius Black. Convicted of killing thirteen people with a single curse, he was said to be the heir apparent to the Dark Lord, Voldemort.Now he has escaped, leaving only two clues as to where he might be headed: Harry Potter's defeat of You-Know-Who was Black's downfall as well. And the Azkaban guards heard Black muttering in his sleep, 'He's at Hogwarts . . . he's at Hogwarts.'Harry Potter isn't safe, not even within the walls of his magical school, surrounded by his friends. Because on top of it all, there may well be a traitor in their midst."
    )
    harry_potter_and_the_goblet_of_fire = Book(
        title="Harry Potter and the Goblet of Fire", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780439139601",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780439139601_p0_v1_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2002-09-01",
        on_hand=10,
        description="Harry Potter is midway through his training as a wizard and his coming of age. Harry wants to get away from the pernicious Dursleys and go to the International Quidditch Cup. He wants to find out about the mysterious event that's supposed to take place at Hogwarts this year, an event involving two other rival schools of magic, and a competition that hasn't happened for a hundred years. He wants to be a normal, fourteen-year-old wizard. But unfortunately for Harry Potter, he's not normal - even by wizarding standards. And in his case, different can be deadly."
    )
    harry_potter_and_order_of_the_phoenix = Book(
        title="Harry Potter and the Order of the Phoenix", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780439358071",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780439358071_p0_v4_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2004-09-01",
        on_hand=10,
        description="The most eagerly anticipated book in history becomes the biggest paperback release of 2004! The book that took the world by storm....In his fifth year at Hogwart's, Harry faces challenges at every turn, from the dark threat of He-Who-Must-Not-Be- Named and the unreliability of the government of the magical world to the rise of Ron Weasley as the keeper of the Gryffindor Quidditch Team. Along the way he learns about the strength of his friends, the fierceness of his enemies, and the meaning of sacrifice."
    )
    harry_potter_and_the_half_blood_prince = Book(
        title="Harry Potter and the Half Blood Prince", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780439785969",
        price=12.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780439785969_p0_v3_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2006-09-01",
        on_hand=10,
        description="The war against Voldemort is not going well; even the Muggles have been affected. Dumbledore is absent from Hogwarts for long stretches of time, and the Order of the Phoenix has already suffered losses. And yet . . . As with all wars, life goes on. Sixth-year students learn to Apparate. Teenagers flirt and fight and fall in love. Harry receives some extraordinary help in Potions from the mysterious Half-Blood Prince. And with Dumbledore's guidance, he seeks out the full, complex story of the boy who became Lord Voldemort — and thus finds what may be his only vulnerability."
    )
    harry_potter_and_the_deathly_hallows = Book(
        title="Harry Potter and the Deathly Hallows", 
        author_first_name="J. K.",
        author_last_name="Rowling", 
        genre="Fantasy",
        format="Paperback",
        isbn="9780545139700",
        price=14.99,
        front_image="https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9780545139700_p0_v5_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D",
        back_image=None,
        publisher="Scholastic, Inc.",
        publication_date="2009-07-07",
        on_hand=10,
        description="It all comes down to this - a final faceoff between good and evil. You plan to pull out all the stops, but every time you solve one mystery, three more evolve. Do you stay the course you started, despite your lack of progress? Do you detour and follow a new lead that may not help? Do you listen to your instincts, or your friends? Lord Voldemort is preparing for battle and so must Harry. With Ron and Hermione at his side, he's trying to hunt down Voldemort's Horcruxes, escape danger at every turn, and find a way to defeat evil once and for all. How does it all end? Find out in Harry Potter and the Deathly Hallows."
    )
    

    


    db.session.add(haunting_of_hill_house) #1 Horror
    db.session.add(frankenstein) #2 Horror
    db.session.add(something_wicked_this_way_comes) #3 Horror
    db.session.add(slade_house) #4 Horror
    db.session.add(black_chalk) #5 Fiction
    db.session.add(the_picture_of_dorian_gray) #6 Horror
    db.session.add(the_metamorphosis) #7 Fiction
    db.session.add(in_cold_blood) #8 True Crime
    db.session.add(bunny) #9 Horror
    db.session.add(brave_new_world) #10 Science Fiction
    db.session.add(wired_that_way) #11 Self Help
    db.session.add(start_with_why) #12 Self Help
    db.session.add(tiny_habits) #13 Self Help
    db.session.add(atomic_habits) #14 Self Help
    db.session.add(the_four_agreements) #15 Self Help
    db.session.add(on_earth_were_briefly_gorgeous) #16 Fiction
    db.session.add(the_buddha_in_the_attic) #17 Fiction
    db.session.add(fight_club) #18 Thriller
    db.session.add(the_burning_girls) #19 Horror
    db.session.add(house_of_leaves) #20 Horror
    db.session.add(the_secret_history) #21 Fiction
    db.session.add(the_midnight_library) #22 Fiction
    db.session.add(firekeepers_daughter) # 23 Young adult
    db.session.add(where_the_crawdads_sing) #24 Fiction
    db.session.add(stardust) #25 Fantasy
    db.session.add(in_a_dark_dark_wood) #26 Thriller
    db.session.add(the_goldfinch) #27 Fiction
    db.session.add(the_little_friend) #28 Fiction
    db.session.add(fahrenheit_451) #29 Science Fiction
    db.session.add(catcher_in_the_rye) #30 Fiction
    db.session.add(the_ex_hex) #31 Romance
    db.session.add(hollywood_wives) #32 Romance
    db.session.add(valley_of_the_dolls) #33 Romance
    db.session.add(anna_karenina) #34 Romance
    db.session.add(the_omnivores_dilemma) #35 Nonfiction
    db.session.add(the_billionaires_vinegar) #36 Nonfiction
    db.session.add(the_big_burn) #37 Nonfiction
    db.session.add(the_yosemite) #38 Nonfiction
    db.session.add(the_art_thief) #39 Nonfiction
    db.session.add(a_house_in_the_sky) #40 Autobiography
    db.session.add(educated) #41 Autobiography
    db.session.add(the_glass_castle) #42 Autobiography
    db.session.add(making_it_so) #43 Authobiography
    db.session.add(i_am_not_your_perfect_mexican_daughter) #44 Young adult
    db.session.add(the_fault_in_our_stars) #45 Young adult
    db.session.add(looking_for_alaska) #46 Young adult
    db.session.add(uglies) #47 Young adult
    db.session.add(the_giver) #48 Young adult
    db.session.add(the_martian) #49 Science Fiction
    db.session.add(do_androids_dream_of_electric_sheep) #50 Science fiction
    db.session.add(the_hobbit) #51 Fantasy
    db.session.add(harry_potter_and_the_sorcerers_stone) # 52 Fantasy/Young Adult
    db.session.add(harry_potter_and_the_chamber_of_secrets) #53 Fantasy/Young Adult
    db.session.add(harry_potter_and_the_prisoner_of_azkaban) #54 Fantasy/Young Adult
    db.session.add(harry_potter_and_the_goblet_of_fire) #55 Fantasy/Young Adult
    db.session.add(harry_potter_and_order_of_the_phoenix) #56 Fantasy/Young Adult
    db.session.add(harry_potter_and_the_half_blood_prince) #57 Fantasy/Young Adult
    db.session.add(harry_potter_and_the_deathly_hallows) #58 Fantasy/Young Adult


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
