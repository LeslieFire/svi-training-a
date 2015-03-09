'''
Written by Antonio Carlos L. Ortiz. Updated: 03/09/2015
Input: Nothing
Output: adds data to the database created on table_def.py
'''

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

#create a Session
#Our handle to the database and let's us interact with it.
Session = sessionmaker(bind=engine)
session = Session()

#Create an artist
new_artist = Artist(name="Bone Thugs and Harmony")
new_artist.albums = [Album(title="E.1999 Eternal",
                           release_date=datetime.datetime.now(),
                           publisher="Ruthless Records",
                           media_type="CD")
                    ]

#add more albums
more_albums = [Album(title="The Crossroads",
                       release_date=datetime.datetime.now(),
                       publisher="Ruthless Records",
                       media_type="CD")
                    ]

new_artist.albums.extend(more_albums)

#Add the record to the session object
session.add(new_artist)
#commit the record the database
session.commit()

#Add several artist
session.add_all([
    Artist(name="Akon"),
    Artist(name="Childish Gambino"),
    Artist(name="Snoop Dogg"),
    ])

session.commit()

