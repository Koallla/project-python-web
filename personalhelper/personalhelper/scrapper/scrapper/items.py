import scrapy


class ScrapperItem(scrapy.Item):
    rating = scrapy.Field()
    logo = scrapy.Field()
    name = scrapy.Field()
    games = scrapy.Field()
    wins = scrapy.Field()
    draws = scrapy.Field()
    losses = scrapy.Field()
    goals_in = scrapy.Field()
    goals_out = scrapy.Field()
    scores = scrapy.Field()
    difference = scrapy.Field()
