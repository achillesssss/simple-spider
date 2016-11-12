import scrapy


class QuotesSpider(scrapy.Spider):
    name = "keyboard"
    start_urls = [
        'http://www.azaudio.vn/ban-phim-co?sort=10',
    ]

    def parse(self, response):
        for item in response.css('figcaption'):
            yield {
                'code': item.css('div.code span::text').extract_first(),
                'brand': item.css('h3 a::text').extract_first(),
                'price': item.css('div.price span.price-new::text').extract_first(),
            }

        next_page = response.css('a.ajaxpagerlink::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
