import json
from itemadapter import ItemAdapter


class ScrapperPipeline:

    def open_spider(self, spider):
        self.file = open('../comands.jl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('logo'):
            line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item