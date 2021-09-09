import scrapy
from crawling.items import ScrapperItem
from scrapy.spiders import CrawlSpider


class FootballSpider(CrawlSpider):
    name = "football"
    allowed_domains = ['football.ua', 'terrikon.com']

    start_urls = ['https://football.ua/ukraine/table.html', 'https://terrikon.com/football/ukraine/championship/' ]


    # def __init__(self, *args, **kwargs):
    #     self.url = kwargs.get('url')
    #     self.domain = kwargs.get('domain')
    #     self.start_urls = [self.url]
    #     self.allowed_domains = [self.domain]


    def parse(self, response):
        rows = response.xpath('//*[@class="main-tournament-table"]//tr')
        rows2 = response.xpath('//*[@id="champs-table"]//tr') 
        comand = ScrapperItem()
        
        
        for row in rows[1:]:
            # comand = {}
            comand['rating'] = row.xpath('td[@class="num"]/text()').get()
            comand['logo'] = row.css('img').attrib['src']
            comand['name'] = row.xpath('td[@class="team"]/a/text()').get()
            comand['games'] = row.xpath('td[@class="games"]/text()').get()
            comand['wins'] = row.xpath('td[@class="win"]/text()').get()        
            comand['draws'] = row.xpath('td[@class="draw"]/text()').get()        
            comand['losses'] = row.xpath('td[@class="lose"]/text()').get()        
            comand['goals_in'] = row.xpath('td[@class="goal"]/text()').get()        
            comand['goals_out'] = row.xpath('td[@class="miss"]/text()').get()        
            comand['difference'] = row.xpath('td[@class="diff"]/text()').get()        
            comand['scores'] = row.xpath('td[@class="score"]/text()').get()        

            yield comand


        for row in rows2[1:]:
            # comand2 = {}
            comand['rating'] = row.css('td::text').get()[:-1]
            comand['name'] = row.xpath('td[@class="team"]/a/text()').get()
            comand['games'] = row.xpath('td[@class="team"]/following-sibling::td/text()').get()
            comand['wins'] = row.xpath('td[@class="win"]/text()').get()
            comand['draws'] = row.xpath('td[@class="draw"]/text()').get()
            comand['losses'] = row.xpath('td[@class="lose"]/text()').get()
            comand['goals_in'] = row.xpath('td[@class="lose"]/following-sibling::td/text()').get()
            comand['goals_out'] = row.xpath('//td[contains(text(), "-")]/following-sibling::td/text()').get()
            comand['scores'] = row.css('strong::text').get()

            yield comand

    



        
