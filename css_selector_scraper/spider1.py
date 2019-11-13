import scrapy
import logging


#from writers import (
#    csv
#    )

logging.getLogger('scrapy').setLevel(logging.WARNING)

class spider1(scrapy.Spider):
    name = 'ATO'
    start_urls = [
        'https://www.ato.gov.au/Media-centre/Media-releases/Fake-car-salesmans-GST-scheme-runs-out-of-gas/',
        'http://mediahub.humanservices.gov.au/media/dont-miss-out-on-north-queensland-floods-assistance/'
        ]

    def parse(self, response):
        
        title_list = response.css('title::text' or 'entry-title::text').extract()
        body_list = response.css('p::text').extract() 
        whole_list = zip(title_list, body_list)#, time_list)

        #Give the extracted content row wise
        for item in zip(title_list,body_list):
            #create a dictionary to store the scraped info
            scraped_info = {
                'body' : item[1],
                'title' : item[0],
            }
            yield scraped_info


# scrapy runspider spider1.py
# virtualenv venv; source ./venv/bin/activate
# pip install scrapy
# scrapy runspider spider1.py
