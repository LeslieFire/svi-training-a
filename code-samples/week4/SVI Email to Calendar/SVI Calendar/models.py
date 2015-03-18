'''
Written by Antonio Carlos L. Ortiz. Updated: 03/18/2015
Input: None
Output: Same as the one in the spider but only used to have a clear reference
what table is being called by database_query.py
'''

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
import settings


DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance.
    """
    return create_engine(URL(**settings.DATABASE))

def create_events_table(engine):
    """
    """
    DeclarativeBase.metadata.create_all(engine)

class Events(DeclarativeBase):
    """Sqlalchemy events model"""
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    summary = Column('summary', String)
    start = Column('start', String, nullable=True)
    end = Column('end', String, nullable=True)
    location = Column('location', String, nullable=True)
    time = Column('time', String, nullable=True)
    link = Column('link', String, nullable=True)
    description = Column('description', String, nullable=True)