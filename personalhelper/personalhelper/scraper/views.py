from django.shortcuts import render 
from .models import Comand
from crawling.crawling.spiders.football_spyder import FootballSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


#   def run_crawl():
#     process = CrawlerProcess(get_project_settings())
#     process.crawl('football_spyder')
#     await process.start()


# def crawl_koovs():
#     settings = get_project_settings()
#     crawler = CrawlerProcess(settings)
#     spider = FootballSpider()
#     crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#     crawler.configure()
#     crawler.crawl(spider)
#     crawler.start()
#     reactor.run(installSignalHandlers=False)

def index(request):

    # crawl_koovs()

    data = Comand.objects.all()

    return render(request, 'comands-table.html', {'comands': data})