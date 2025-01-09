from pathlib import Path

import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://www.ncbi.nlm.nih.gov/gene/?term=ctcf"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        element = response.selector.xpath('/html/body/div[1]/div[1]/form/div[1]/div[4]/div/div[3]/section/div/div/div/div/div/div[1]/div[2]/ul/li').getall()[0]
        gene_id = re.search(r'<li>Gene ID: (\d+)</li>', element).group(1)
        yield gene_id