# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from .models import Comand


class ScrapperItem(scrapy.Item):
    django_model = Comand
    rating = scrapy.Field()
    name = scrapy.Field()
    games = scrapy.Field()
    wins = scrapy.Field()
    draws = scrapy.Field()
    losses = scrapy.Field()
    goals_in = scrapy.Field()
    goals_out = scrapy.Field()
    scores = scrapy.Field()
