'''
Written by Antonio Carlos L. Ortiz. Updated: 03/09/2015
Input: Nothing
Output: Edits the data placed by script data_in.py
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album
from table_def import Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

#create a session
Session = sessionmaker(bind=engine)
session = Session()

#querying for a record in the artist table
#firs() tells we only want the first result.
response = session.query(Artist).filter(Artist.name=="Snoop Dogg").first()
print response.name

#changing the name
response.name = "Snoopy Doggy"
session.commit()

#editing Album data
#filters artists with albums, and the album title with "the crossroads", returns artist and album
artist, album = session.query(Artist, Album).filter(Artist.id==Album.artist_id).filter(Album.title=="The Crossroads").first()
album.title = "Tha Crossroads"
session.commit()