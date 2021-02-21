import scrapy
from scrapy.pipelines.images import ImagesPipeline
from image_downloader.items import ImageItem
from scrapy_splash import SplashRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium import
import time

opts = Options()
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
# opts.add_argument("user-agent=USER_AGENT")

query = "miss lemon poirot"
query = '+'.join(query.split())
url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
# url = ""
# url = 'https://www.csa.iisc.ac.in/'

class ImageSpider(scrapy.Spider):
    name = 'image_downloader'
    allowed_domains = []
    start_urls = [url]

    def __init__(self):
        # self.driver = webdriver.Chrome(chrome_options=opts)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url,self.parse,args={'wait':0.5})

    def parse(self, response):
        # TODO: scrape the larger images

        self.driver.get(response.url)
        # for elem in response.xpath("//img"):



        # for elem in self.driver.find_elements_by_xpath("//img"):
        #     img_url = elem.get_attribute("src")
        #     # img_url = elem.xpath("@src").extract_first()
        #     # print(img_url)
        #     yield ImageItem(image_urls = [img_url] )

        ######## CODE TO ITERATE OVER PAGES OF RESULTS ##########
        # num of result pages you want to scrape
        # PAGES = 1
        # while PAGES:
        #     for elem in self.driver.find_elements_by_xpath("//img"):
        #         img_url = elem.get_attribute("src")
        #         # img_url = elem.xpath("@src").extract_first()
        #         # print(img_url)
        #         yield ImageItem(image_urls=[img_url])
        #
        #     # click the Next button to go to the next result page
        #     try:
        #         next_button = self.driver.find_element_by_xpath("//a[contains(text(),'Next')]")
        #     except:
        #         try:
        #             next_button = self.driver.find_element_by_xpath("//a/span[contains(text(),'>')]")
        #             next_button.click()
        #
        #         except:
        #             pass
        #     PAGES -= 1


        # ############## TO KEEP SCROLLING TILL END OF PAGE #################
        #
        SCROLL_PAUSE_TIME = 0.5
        # SCROLL_Y = 500
        last_height = self.driver.execute_script("return document.body.scrollHeight;")
        #Scroll down to get more images
        while True:
            # Extract images
            elements = self.driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
            for elem in elements:
                elem.click()
                # time.sleep(0.2)
                larger_img = self.driver.find_elements_by_xpath("//img[@class='n3VNCb']")[1]
                img_url = larger_img.get_attribute("src")
                # img_url = elem.get_attribute("src")
                # img_url = elem.xpath("@src").extract_first()
                # print(img_url)
                yield ImageItem(image_urls=[img_url])       # return ImageItem


            # SCROLL_Y = elements[-1].location['y']                   # find y coord of last image scraped
            # scroll as much as that last elem so all the prev images get removed from screen
            # self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(SCROLL_Y) + ")")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            # scroll pause time of 1 sec works. 0.5 becomes too less
            time.sleep(SCROLL_PAUSE_TIME)
            #check if new document height == old doc ht => ht no longer changing => reached bottom of page
            new_height = self.driver.execute_script("return document.body.scrollHeight;")
            if new_height == last_height:
                break
            last_height = new_height




        ############## WITHOUT SCROLLING #######################
        # elements = self.driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
        # for elem in elements:
        #     elem.click()
        #     # time.sleep(0.001)
        #     larger_img = self .driver.find_elements_by_xpath("//img[@class='n3VNCb']")[1]
        #     img_url = larger_img.get_attribute("src")
        #     # img_url = elem.get_attribute("src")
        #     # img_url = elem.xpath("@src").extract_first()
        #     # print(img_url)
        #     # yield ImageItem(image_urls=[img_url])       # return ImageItem

        time.sleep(1000)

        self.driver.close()



