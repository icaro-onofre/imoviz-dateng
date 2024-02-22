import scrapy
from scrapy.spiders import CrawlSpider, Rule


class VivaRealSpider(CrawlSpider):
    name = "viva_real"
    allowed_domains = ["www.vivareal.com.br"]
    start_urls = ["https://www.vivareal.com.br/venda/sp/sao-paulo/"]

    def start_requests(self):
        urls = [
            "https://www.vivareal.com.br/venda/sp/sao-paulo/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for imoveis in response.xpath("/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[19]/div/article/a"):
            print(imoveis.css(".property-card__price").get())
        pass
