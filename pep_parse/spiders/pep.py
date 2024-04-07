import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        number, name = response.xpath(
            '//h1[@class="page-title"]/text()'
        ).get().split(' – ', 1)

        status = response.xpath(
            '//dl[contains(@class, "rfc2822")]'
            '/dt[contains(text(), "Status")]'
            '/following-sibling::dd/abbr/text()'
        ).get()

        yield PepParseItem(
            {
                'number': int(number.split()[1]),
                'name': name,
                'status': status,
            }
        )

    def parse(self, response):
        peps = response.xpath('//section[@id="numerical-index"]/*/tbody/tr')
        pep_links = peps.xpath(
            'td/a[contains(@class, "pep")]/@href').getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)
