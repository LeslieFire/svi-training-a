#!usr/bin/bash

#this is just a script to use on a cronjob to automatically schedule the run of the crawler.

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
# source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

cd /home/antonio/SVI/'SVI Email to Calendar'/my_scraper/crunchbase_scraper

pwd
workon ScrapeProj
scrapy crawl crunchbaseevents
deactivate
