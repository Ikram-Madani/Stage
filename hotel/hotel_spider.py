import scrapy
from hotel.items import HotelSentimentItem
from datetime import datetime
import re

class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["www.tripadvisor.com"]

    def start_requests(self):

        urls = [
         "https://www.tripadvisor.com/Hotels-g297941-Djerba_Island_Medenine_Governorate-Hotels.html"]
   

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):

        for href in response.xpath('//div[@class="listing_title"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_hotel)

  
def parse_hotel(self, response):
        for href in response.xpath('//div[@id="component_1"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_review)



def parse_review(self, response):
        item = HotelSentimentItem()
        item['title'] = response.xpath('//div[@class="hotels-hotel-review-about-with-photos-Reviews__ratingLabel--24XY2"]/descendant::text()').extract() 
   #  item['content'] = response.xpath('//span[@class="hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA"]/text()').extract()
       #item['stars'] = response.xpath('//span[@class="ui_bubble_rating bubble_45"]/img/@alt').extract()[0]
        #return item
 #title= response.xpath('//div/h1/text()').extract_first() 
 #print(title)
       

