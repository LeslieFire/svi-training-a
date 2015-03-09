#!usr/bin/bash

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
# source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

cd /home/antonio/SVI/Scrapy/Tutorial/scrapy-tutorial-newcoder/Projects/new-coder/scrape_workspace/my_scraper

workon ScrapeProj
scrapy crawl livingsocial
deactivate
