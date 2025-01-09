# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:
    def open_spider(self, spider):
        self.fd = open('summary.txt', 'w')

    def process_item(self, item, spider):
        self.fd.write(item['summary'] + '\n')
        return item

    def close_spider(self, spider):
        self.fd.close()