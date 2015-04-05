'''
Written by Antonio Carlos L. Ortiz. Updated: 04/05/2015
Input: None
Output: Same as the one in the scraper and is also used to call the
database.
'''

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',
	'password': 'stangg123',
	'database': 'scrape_crunchbase'
}

try:
	from .local_settings import *
except ImportError:
	pass