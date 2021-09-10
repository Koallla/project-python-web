from itemadapter import ItemAdapter
from scraper.models import Comand


class CrawlingPipeline(object):
    if Comand.objects.all():
        Comand.objects.all().delete()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('logo'):
            item.save()
            return item
    
