from itemadapter import ItemAdapter
from scraper.models import Comand


class CrawlingPipeline(object):

    def process_item(self, item, spider):
        c = Comand()
        c.rating = item['rating']
        c.logo = item['logo']
        c.name = item['name']
        c.games = item['games']
        c.wins = item['wins']
        c.draws = item['draws']
        c.losses = item['losses']
        c.goals_in = item['goals_in']
        c.goals_out = item['goals_out']
        c.scores = item['scores']
        c.difference = item['difference']
        c.save()
        return item

    
