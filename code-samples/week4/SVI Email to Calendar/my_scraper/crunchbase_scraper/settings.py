BOT_NAME = 'crunchbaseevents'

SPIDER_MODULES = ['crunchbase_scraper.spiders']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',
	'password': 'secret',
	'database': 'crunch_base_events_scrape_db'
}

ITEM_PIPELINES = ['crunchbase_scraper.pipelines.CrunchBaseEventsPipeline']