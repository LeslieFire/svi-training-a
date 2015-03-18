'''
Written by Antonio Carlos L. Ortiz. Updated: 03/18/2015
Input: None
Output: to create a dictionary like object from scraped data.
'''


from scrapy.item import Item, Field

class CrunchBaseEvent(Item):
	"""
	CrunchBaseEvents container (dictionary-like object) for scraped data.
	"""
	summary = Field()
	start = Field()
	end = Field()
	location = Field()
	time = Field()
	link = Field()
	description = Field()