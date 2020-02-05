import scrapy
from hotel.items import ProjikramItem
from scrapy import Spider
from scrapy.selector import Selector
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
            yield scrapy.Request(url, callback=self.parse_review)

   



    def parse_review(self, response):
        item = ProjikramItem()

        item['title'] =response.xpath('//div[@class="hotels-hotel-review-about-with-photos-Reviews__ratingLabel--24XY2"]/descendant::text()').extract()
     
        
        item['content'] = response.xpath('//span[@class="hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA"]/text()').extract()[0]
    # item['date']=response.xpath('//span[@class="location-review-review-list-parts-EventDate__event_date--1epHa"]/text()').extract()[0]
      #item['comments'] = response.xpath('//div[@class="cPQsENeY"]/descendant::text()').extract()[0]
         
       #item['stars'] = response.xpath('//span[starts-with(@class, "rating")]/span/@alt').extract()[0].replace('bubble', 'star')
        item['data']= response.xpath('//div[@class="cPQsENeY"]/text()').extract()[0]
    # item['name'] =  response.xpath('//div[@class="social-member-event-MemberEventOnObjectBlock__event_type--3njyv"]/descendant::text()').extract()[0]

        return item
