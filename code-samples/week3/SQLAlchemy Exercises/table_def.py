'''
Written by Antonio Carlos L. Ortiz. Updated: 03/09/2015
Input: nothing
Output: Creates a database with tables and columns defined below.
'''

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

#the engine object is where the database connection information.
#it makes connection to the database possible. 
engine = create_engine('sqlite:///mymusic.db', echo=True)

DeclarativeBase = declarative_base()

class Artist(DeclarativeBase):
	"""
	SQLAlchemy artists model.
	"""
	__tablename__ = "artists" 

	id = Column(Integer, primary_key=True)
	name = Column(String)

class Album(DeclarativeBase):
	"""
	SQLAlchemy albums model.
	"""
	__tablename__ = "albums"

	#no column names because sqlite uses variablenames as default. Not sure for Postgresql tho.
	id = Column(Integer, primary_key=True)
	title = Column(String)
	release_date = Column(Date)
	publisher = Column(String)
	media_type = Column(String)

	#the relationship directive tells SQLAlchemy to tie the Album class/table to the artist.
	#many to one relationships. Many albums to one artist.
	artist_id = Column(Integer, ForeignKey("artists.id"))
	artist = relationship("Artist", backref=backref("albums", order_by=id))

#create tables
DeclarativeBase.metadata.create_all(engine)