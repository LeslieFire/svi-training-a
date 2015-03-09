from sqlalchemy.orm import sessionmaker
from models import Deals
from models import db_connect
from models import create_deals_table

class LivingSocialPipeline(object):
	"""Livingsocial pipeline for storing items in the database."""
	def __init__(self):
		"""
		Initializes database connection and sessionmaker.
		Creates deals table.
		"""
		engine = db_connect()
		create_deals_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		"""
		Save deals in the database.
		This method is called for every item pipeline component.
		"""
		session = self.Session()
		deal = Deals(**item)
		try:
			session.add(deal)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item
