#!usr/bin/bash
cd /home/antonio/SVI/'SVI Email to Calendar'/my_scraper/crunchbase_scraper

pwd
workon ScrapeProj
scrapy crawl crunchbaseevents_spider
scrapy crawl crunchbaseevents_others_spider
scrapy crawl crunchbaseenvets_accelerator_spider
deactivate
