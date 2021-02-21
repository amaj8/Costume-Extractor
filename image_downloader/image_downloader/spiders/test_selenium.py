# # # TODO: Why does this file get executed when I run "scrapy crawl image_downloader"?
# import scrapy
# from scrapy.pipelines.images import ImagesPipeline
# # from image_downloader.items import ImageItem
# from scrapy_splash import SplashRequest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # from selenium import
# import time
# # #
# # # opts = Options()
# # # # TODO: adding user agent decreases #results. Why? All results displayed when no user agent is given.
# # # # USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# # # # opts.add_argument("user-agent=USER_AGENT")
# # #
# query = 'poirot david suchet'
# query = '+'.join(query.split())
# url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
# # url = ""
# # url = 'https://www.csa.iisc.ac.in/'
#
# # driver = webdriver.Chrome(chrome_options=opts)
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)
# elements = driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
# for elem in elements:
#     elem.click()
#     time.sleep(1)
#     larger_img = driver.find_elements_by_xpath("//img[@class='n3VNCb']")[1]
#     # time.sleep(100)
#     img_url = larger_img.get_attribute("src")
#     # print(larger_img.get_attribute("class"))
#
#     print(img_url)
#     # img_url = elem.xpath("@src").extract_first()
#     # print(img_url)
#     # yield ImageItem(image_urls=[img_url])       # return ImageItem
# #
# # #
# # # # class ImageSpider(scrapy.Spider):
# # # #     name = 'image_downloader'
# # # #     allowed_domains = []
# # # #     start_urls = [url]
# # # #
# # # #     def __init__(self):
# # # #         self.driver = webdriver.Chrome(chrome_options=opts)
# # # #
# # # #
# # # #     # def start_requests(self):
# # # #     #     for url in self.start_urls:
# # # #     #         yield SplashRequest(url,self.parse,args={'wait':0.5})
# # # #
# # # #     def parse(self, response):
# # # #         # TODO: scrape the larger images
# # # #         self.driver.get(response.url)
# # # #         # for elem in response.xpath("//img"):
# # # #
# # # #         # num of result pages you want to scrape
# # # #         PAGES = 4
# # # #         # for elem in self.driver.find_elements_by_xpath("//img"):
# # # #         #     img_url = elem.get_attribute("src")
# # # #         #     # img_url = elem.xpath("@src").extract_first()
# # # #         #     # print(img_url)
# # # #         #     yield ImageItem(image_urls = [img_url] )
# # # #
# # # #         while PAGES:
# # # #             for elem in self.driver.find_elements_by_xpath("//img"):
# # # #                 img_url = elem.get_attribute("src")
# # # #                 # img_url = elem.xpath("@src").extract_first()
# # # #                 # print(img_url)
# # # #                 yield ImageItem(image_urls=[img_url])
# # # #
# # # #             # click the Next button to go to the next result page
# # # #             try:
# # # #                 next_button = self.driver.find_element_by_xpath("//a[contains(text(),'Next')]")
# # # #             except:
# # # #                 # try:
# # # #                 next_button = self.driver.find_element_by_xpath("//a/span[contains(text(),'>')]")
# # # #                 # except:
# # # #                 #     time.sleep(1000)
# # # #             next_button.click()
# # # #             PAGES -= 1
# # # #
# # # #         # SCROLL_PAUSE_TIME = 10000
# # # #         # SCROLL_Y = 1000
# # # #         # last_height = self.driver.execute_script("return document.body.scrollHeight;")
# # # #         # #Scroll down to get more images
# # # #         # while True:
# # # #         #     # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# # # #         #     self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(SCROLL_Y) + ")")
# # # #         #     time.sleep(SCROLL_PAUSE_TIME)
# # # #         #     new_height = self.driver.execute_script("return document.body.scrollHeight;")
# # # #         #     if new_height == last_height:
# # # #         #         break
# # # #         #     last_height = new_height
# # # #         #
# # # #         #     for elem in self.driver.find_elements_by_xpath("//img"):
# # # #         #         img_url = elem.get_attribute("src")
# # # #         #         # img_url = elem.xpath("@src").extract_first()
# # # #         #         # print(img_url)
# # # #         #         yield ImageItem(image_urls=[img_url])
# # # #
# # # #         # time.sleep(1000)
# # # #
# # # #         self.driver.close()
# # # #
# # # #
# # # #
