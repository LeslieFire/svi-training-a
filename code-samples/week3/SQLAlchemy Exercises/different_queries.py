'''
Written by Antonio Carlos L. Ortiz. Updated: 03/09/2015
Input: Nothing
Output: Different Queries. This is just to test how to queries on different situations.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist


engine = create_engine('sqlite:///mymusic.db', echo=False)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# how to do a SELECT * (i.e. all)
response = session.query(Artist).all()
for artist in response:
	print artist.name

# how to sort the results (ORDER BY)
response = session.query(Album).order_by(Album.title).all()
for album in response:
	print album.title

# how to SELECT the first result
response = session.query(Artist).filter(Artist.name=="Snoop Doggy").first()
print response

# how to do a JOINed query
query_ = session.query(Artist, Album)
query_ = query_.filter(Artist.id==Album.artist_id)
artist, album = query_.filter(Album.title=="Tha Crossroads").first()
print artist.name, album.title

response = session.query(Album).filter(Album.publisher.like("R%")).all()
for item in response:
	print item.publisher