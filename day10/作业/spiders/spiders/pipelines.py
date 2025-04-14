# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def open_spider(self, spider):
        if spider.name == 'quotes':
            self.client = pymongo.MongoClient()
            self.db = self.client.get_database('quotes')
            self.db.drop_collection('quotes')
            self.collection = self.db.create_collection('quotes')


    def process_item(self, item, spider):
        if spider.name == 'quotes':
            self.collection.insert_one(item)
        return item

    def close_spider(self, spider):
        if spider.name == 'quotes':
            self.client.close()