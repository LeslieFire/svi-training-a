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