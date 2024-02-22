import scrapy
from scrapy.spiders import CrawlSpider, Rule

class Imovel():
    def __init__(self,preco,metragem,endereco):
        self.endereco=endereco

    endereco
    preco 
    metragem

    def _endereco(self):
        return endereco
    def _endereco_set(self,endereco):
        endereco=endereco


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
        imovel = Imovel()
        for imoveis in response.xpath("/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[19]/div/article/a").getall():
            yield {"metragem":metragem}
        pass
