import scrapy


class GatewayfirstItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
