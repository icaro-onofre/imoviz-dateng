# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImovizcrawlerPipeline:
    def process_item(self, item, spider):
        scrapped = ItemAdapter(item)
        print("Dentro do pipeline",scrapped.get("imoveis_preco"))
        print("Dentro do pipeline",scrapped.get("imoveis_endereco"))
        return item
