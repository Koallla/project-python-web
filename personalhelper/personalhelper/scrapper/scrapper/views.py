
from django import template
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.template import loader

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapper.scrapper.spiders.football_spyder import FootballSpider




def index(request):
    # process = CrawlerProcess()
    # process.crawl(FootballSpider)
    # process.start()
    return render(request, 'comands.html')
