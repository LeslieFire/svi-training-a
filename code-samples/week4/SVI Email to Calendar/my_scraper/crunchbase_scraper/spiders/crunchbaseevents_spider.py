from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import os

from crunchbase_scraper.items import CrunchBaseEvent

class CrunchBaseEventsSpider(BaseSpider):
    """Spider for the CrunchBase Events Newsletter"""
    name = "crunchbaseevents_spider"
    allowed_domains = ["crunchbase.com"]
    start_urls = []
    
    #where the local files are
    url_dir = '/home/antonio/SVI/SVI Email to Calendar/Email Scraping/out_dir'

    for subdir, dirs, files in os.walk(url_dir):
        for file in files:
            start_url = os.path.join(subdir, file)
            start_url = 'file://' + start_url

            start_urls.append(start_url)

    events_list_xpath = '//tr[@style="display: block; padding-top: 20px;"]'
    
    #'title':'.//span[@itemscope]/meta[@itemprop="name"]/@content', 
    #element li with dealid parameter, element span with itemscope parameter,
    #element meta with itemprop parameter with value "name",  return the value 
    #of parameter content.

    #check the source first rather than the DOM that was interpreted by the browser.
    item_fields = {    
                   'description':   './/td/table/tbody/tr/td/table[@style]/tbody/td/text()',
                   'summary':       './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[1]/tbody/tr/td/a/text()',
                   'link':          './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[1]/tbody/tr/td/a/@href',
                   'start':         './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/text()',
                   'end':           './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/text()',
                   'location':      './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[2]/tbody/tr[3]/td[2]/text()',
                   'time':          './/td/table/tbody/tr/td/table[@border]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/text()',
                   }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses
        """
        selector = HtmlXPathSelector(response)

        #iterate over events
        for event in selector.select(self.events_list_xpath):
            loader = XPathItemLoader(CrunchBaseEvent(), selector=event)

            #define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            #iterate over fields and add xpaths to the loader.
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)

            yield loader.load_item()