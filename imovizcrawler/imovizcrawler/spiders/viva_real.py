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
        i = 1
        for imoveis in range(20):
            i+=1
            yield {"imoveis_preco":response.xpath(f"/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[%i]/div/article/a"%i).css(".property-card__price").getall(),
                   "imoveis_endereco":response.xpath(f"/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[%i]/div/article/a/div/h2/span[2]/span[1]"%i).css(".property-card__address").getall()}
