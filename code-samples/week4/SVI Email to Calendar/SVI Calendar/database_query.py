'''
Written by Antonio Carlos L. Ortiz. Updated: 04/05/2015
Input: None
Output: to query the database and return a dict object that is fashioned to the requirement
of the google calendar api.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

from models import Events
from pprint import pprint
from stringtodate import stringtodate

import settings

def query():
    engine = create_engine(URL(**settings.DATABASE))

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    table_list = []

    response = session.query(Events).all()
    for event in response:
        table_dict = {}
        start_dict = {}
        end_dict = {}
        for attribute in dir(event):
            if 'unicode' in str(type(attribute)):
                table_dict[attribute] = getattr(event, attribute)   

        table_dict['end'] = stringtodate(getattr(event,'end'),'end')        
              
        if table_dict['start'] is None:
            table_dict['start'] = table_dict['end']
        else:
            table_dict['start'] = stringtodate(getattr(event,'start'),'start')

        start_dict['date'] = table_dict['start']
        end_dict['date'] = table_dict['end']

        table_dict['start'] = start_dict
        table_dict['end'] = end_dict

        time = getattr(event, 'time')

        if 'unicode' in str(type(time)):
            time = time.replace("\r\n", " ")

        if time is None:
            time = ' '

        link = getattr(event, 'link')
        description = getattr(event, 'description')

        table_dict['description'] = ' '.join([description, time, link])

        table_dict.pop('time', None)
        table_dict.pop('link', None)

        table_list.append(table_dict)
    
    return table_list

if __name__ == "__main__":
    pprint(query())