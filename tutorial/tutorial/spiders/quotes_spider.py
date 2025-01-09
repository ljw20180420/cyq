from pathlib import Path

import scrapy
import re
from ..items import SummaryItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "https://www.ncbi.nlm.nih.gov/gene/10664"
    ]

    def parse(self, response):
        summaryDl = response.xpath('//*[@id="summaryDl"]')
        summary = summaryDl.xpath('//dt[text()="Summary"]/following-sibling::node()[2]')[0]
        item = SummaryItem(summary = summary.xpath('string(.)').extract()[0])
        yield item