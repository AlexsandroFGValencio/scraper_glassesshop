# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        products = response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for product in products:
            product_name = (product.xpath(".//div[position()=3]/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-title']/a[@href]/text()").get()).strip()
            product_link = response.urljoin(product.xpath(".//div[position()=3]/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-title']/a[@href]/@href").get())
            product_price = product.xpath(".//div[position()=3]/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6'][position()=2]/div[@class='p-price']/div/span/text()").get()
            product_image_url = response.urljoin(product.xpath(".//div[@class='product-img-outer']/a[@href]/img[@class='lazy d-block w-100 product-img-default']/@data-src").get())

            yield {
                'product_name': product_name,
                'product_link': product_link,
                'product_price': product_price,
                'product_image_url': product_image_url
            }
