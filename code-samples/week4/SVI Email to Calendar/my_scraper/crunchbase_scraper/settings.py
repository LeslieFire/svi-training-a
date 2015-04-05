BOT_NAME = 'crunchbaseevents'

SPIDER_MODULES = ['crunchbase_scraper.spiders']

DATABASE = {
	'drivername': '',
	'host': 'localhost',
	'port': '5432',
	'username': '',
	'password': '',
	'database': ''
}

ITEM_PIPELINES = ['crunchbase_scraper.pipelines.CrunchBaseEventsPipeline']

try:
	from .local_settings import *
except ImportError:
	pass