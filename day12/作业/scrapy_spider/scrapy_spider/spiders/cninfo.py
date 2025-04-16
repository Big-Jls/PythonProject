import json
import scrapy


class CninfoSpider(scrapy.Spider):
    name = "cninfo"

    def start_requests(self):
        url = "https://www.cninfo.com.cn/new/hisAnnouncement/query"
        formdatas = [{
            'pageNum': f'{i}',
            'pageSize': '30',
            'column': 'szse',
            'tabName': 'fulltext',
            'seDate': '2024-10-16~2025-04-17',
            'isHLtitle': 'true'
        } for i in range(1, 3)]
        for formdata in formdatas:
            yield scrapy.FormRequest(url=url, formdata=formdata)

    def parse(self, response):
        result = response.text
        result = json.loads(result)
        announcements = result['announcements']
        for announcement in announcements:
            secCode = announcement['secCode']
            orgId = announcement['orgId']
            announcementId = announcement['announcementId']
            title = announcement['announcementTitle']
            file_url = announcement['adjunctUrl']  # 这里应该从announcement中获取实际的URL
            data = {
                'secCode': secCode,
                'announcementId':announcementId,
                'orgId': orgId,
                'title': title,
                'file_url': file_url
            }
            yield scrapy.Request(url=f'https://static.cninfo.com.cn/{file_url}', callback=self.file_parse, meta=data)

    def file_parse(self, response):
        item = response.body
        item_dict = response.meta
        item_dict.update({'content': item})
        yield item_dict