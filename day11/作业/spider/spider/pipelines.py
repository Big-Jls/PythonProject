# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def __init__(self):
        self.download_folder = 'downloads'
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

    def process_item(self, item, spider):
        content = item['content']
        url = item['url']
        file_name = os.path.join(self.download_folder, url.split("/")[-1])
        with open(file_name, 'wb') as f:
            f.write(content)
        return item
