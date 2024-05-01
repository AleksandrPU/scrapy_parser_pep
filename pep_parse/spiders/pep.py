import scrapy
from tqdm.asyncio import tqdm

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        number, name = response.xpath(
            '//h1[contains(@class, "page-title")]/text()'
        ).get().split(' – ', 1)

        status = response.xpath(
            '//dl[contains(@class, "rfc2822")]'
            '//dt[normalize-space(.)="Status:"]'
            '/following-sibling::dd[1]//text()'
        ).get()

        yield PepParseItem(
            {
                'number': int(number.split()[1]),
                'name': name,
                'status': status,
            }
        )

    def parse(self, response, **kwargs):
        pep_links = response.xpath(
            '//section[@id="numerical-index"]//td[2]//@href'
        ).getall()

        for link in tqdm(pep_links):
            yield response.follow(link, callback=self.parse_pep)
