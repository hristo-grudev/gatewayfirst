import scrapy

from scrapy.loader import ItemLoader

from ..items import GatewayfirstItem
from itemloaders.processors import TakeFirst


class GatewayfirstSpider(scrapy.Spider):
	name = 'gatewayfirst'
	start_urls = ['https://www.gatewayfirst.com/ABOUT-US/Newsroom']

	def parse(self, response):
		post_links = response.xpath('//div[@class="DefaultContainer"]//div[@class="Normal"]')
		for post in post_links[1:-4]:
			title = post.xpath('.//h3//text()[normalize-space()]').get()
			description = post.xpath(
				'.//*[not(ancestor::h1)]//text()[normalize-space()]').getall()
			description = [p.strip() for p in description if '{' not in p]
			description = ' '.join(description).strip()

			item = ItemLoader(item=GatewayfirstItem(), response=response)
			item.default_output_processor = TakeFirst()
			item.add_value('title', title)
			item.add_value('description', description)

			yield item.load_item()
