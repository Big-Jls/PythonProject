# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyP1Pipeline:
    def open_spider(self, spider):
        if spider.name == 'quotes':
            self.client = pymongo.MongoClient()
            self.client.drop_database("quotes")
            self.db = self.client.get_database("quotes")
            self.collection = self.db.get_collection("quotes")

            self.datas = []

    def process_item(self, item, spider):
        if spider.name == 'quotes':
            self.datas.append(item)
            if len(self.datas) == 10:
                self.collection.insert_many(self.datas)
                self.datas.clear()
        return item

    def close_spider(self, spider):
        if spider.name == 'quotes':
            if self.datas:
                self.collection.insert_many(self.datas)
            self.client.close()
