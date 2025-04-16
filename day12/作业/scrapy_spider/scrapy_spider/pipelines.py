import os
import pymongo

class ScrapySpiderPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.db = self.client.get_database('cninfo')
        self.collection = self.db.get_collection('info')

    def process_item(self, item, spider):
        os.makedirs('./info', exist_ok=True)
        if isinstance(item, dict) and 'title' in item:
            title = item['title']
            valid_title = "".join([c for c in title if c.isalnum() or c in (' ', '-', '_')])
            file_path = os.path.join('./info', f'{valid_title}.pdf')
            with open(file_path, 'wb') as f:
                f.write(item.pop('content'))
            self.collection.insert_one(item)
        return item