import scrapy
from scrapper.items import ScrapperItem


class FootballSpider(scrapy.Spider):
    name = "football"
    allowed_domains = ['terrikon.com'
    #  'football.ua'
    ]

    start_urls = ['https://terrikon.com/football/ukraine/championship/'
    # 'https://football.ua/ukraine/table.html'
    ]

    # def __init__(self, *args, **kwargs):
    #     self.url = kwargs.get('url')
    #     self.domain = kwargs.get('domain')
    #     self.start_urls = [self.url]
    #     self.allowed_domains = [self.domain]


    def parse(self, response):
        rows = response.xpath('//*[@id="champs-table"]//tr')
        comand = ScrapperItem()
        for row in rows[1:]:
            
            # comand = {}
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
