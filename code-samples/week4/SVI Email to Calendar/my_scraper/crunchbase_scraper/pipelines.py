from sqlalchemy.orm import sessionmaker
from models import Events
from models import db_connect
from models import create_events_table

class CrunchBaseEventsPipeline(object):
	"""CrunchBaseEvents pipeline for storing items in the database."""
	def __init__(self):
		"""
		Initializes database connection and sessionmaker.
		Creates deals table.
		"""
		engine = db_connect()
		create_events_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		"""
		Save events in the database.
		This method is called for every item pipeline component.
		"""

		session = self.Session()
		event = Events(**item)

		if 'others' in str(spider):
			event.summary = 'Other Event: ' + event.summary
		elif 'accelerator' in str(spider):
			event.summary = 'Accelerator Deadline: ' + event.summary

		try:
			session.add(event)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item
