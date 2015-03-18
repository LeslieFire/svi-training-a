'''
Written by Antonio Carlos L. Ortiz. Updated: 03/18/2015
Input: None
Output: Just the settings of the scraper to know what database 
the spider should connect to.
'''
BOT_NAME = 'crunchbaseevents'

SPIDER_MODULES = ['crunchbase_scraper.spiders']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',
	'password': '*****',
	'database': 'crunch_base_events_scrape_db'
}

ITEM_PIPELINES = ['crunchbase_scraper.pipelines.CrunchBaseEventsPipeline']