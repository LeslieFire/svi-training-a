'''
Written by Antonio Carlos L. Ortiz. Updated: 03/18/2015
Input: None
Output: to query the specified database on settings.py
and return a dict object that is fashioned to the requirement
of the google calendar api.
'''

#this required local virtualon ScrapeProj

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Events
from sqlalchemy.engine.url import URL
import settings
from pprint import pprint
from stringtodate import string2date

def query():
	engine = create_engine(URL(**settings.DATABASE))

	# create a Session
	Session = sessionmaker(bind=engine)
	session = Session()

	table_list = []
	tablename = Events

	response = session.query(tablename).all()
	for event in response:
		table_dict = {}
		start_dict = {}
		end_dict = {}
		for attribute in dir(event):
			if 'unicode' in str(type(attribute)):
				table_dict[attribute] = getattr(event, attribute)	

		table_dict['start'] = string2date(getattr(event,'start'),'start')
		table_dict['end'] = string2date(getattr(event,'end'),'end')		
		
		if table_dict['end'] is None:
			table_dict['end'] = table_dict['start']

		start_dict['date'] = table_dict['start']
		end_dict['date'] = table_dict['end']

		table_dict['start'] = start_dict
		table_dict['end'] = end_dict

		time = getattr(event, 'time')
		time = time.replace("\r\n", " ")

		link = getattr(event, 'link')
		description = getattr(event, 'description')
		table_dict['description'] = ' '.join([description, time, link])

		table_dict.pop('time', None)
		table_dict.pop('link', None)

		table_list.append(table_dict)
	
	return table_list

if __name__ == "__main__":
	query()	