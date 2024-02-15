from Entities.Item import Item
import Util
from bs4 import BeautifulSoup
from typing import List
import time
from selenium.webdriver.common.by import By


class ItemsPage(object):
    def __init__(self, driver, config_data):
        self.driver = driver
        self.config_data = config_data

    def get_price_estimate(self, data):
        estimate_div = self.config_data['ITEM_DETAILS']['ESTIMATE_PRICE']
        estimate = data.findAll('p', class_=estimate_div)[1].text
        return estimate

    def get_price_sold(self, data):
        price_div = self.config_data['ITEM_DETAILS']['PRICE_SOLD']
        price_sold = Util.get_text(data, 'p', price_div)
        return price_sold

    def get_item_format_1(self, item_info):
        if Util.get_text(item_info, 'p', self.config_data['ITEM_DETAILS_FORMAT_1']['AUTHOR']) == 'n/a':
            author = 'n/a'
            title = Util.get_text(item_info, 'p', self.config_data['ITEM_DETAILS_FORMAT_1']['TITLE_1'])
        else:
            author = Util.get_text(item_info, 'p', self.config_data['ITEM_DETAILS_FORMAT_1']['AUTHOR'])
            title = Util.get_text(item_info, 'p', self.config_data['ITEM_DETAILS_FORMAT_1']['TITLE_2'])

        print(title)
        estimated_price = self.get_price_estimate(item_info)
        price_sold = self.get_price_sold(item_info)
        item = Item(author, title, estimated_price, price_sold)
        return item

    def get_item_format_2(self, item_info):
        author = Util.get_text(item_info, 'h5', self.config_data['ITEM_DETAILS_FORMAT_2']['AUTHOR'])
        title = Util.get_text(item_info, 'p', self.config_data['ITEM_DETAILS_FORMAT_2']['TITLE'])
        print(title)
        estimated_price = self.get_price_estimate(item_info)
        price_sold = self.get_price_sold(item_info)
        item = Item(author, title, estimated_price, price_sold)
        return item

    def get_items_on_page(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, parser='html.parser', features="lxml")
        item_list_div = self.config_data['ITEM_DETAILS_FORMAT_1']['ITEM_LIST']
        data = soup.findAll('div', item_list_div)

        if len(data) != 0:
            print('format 1')
            items_list_div = self.config_data['ITEM_DETAILS_FORMAT_1']['ITEM_LIST']
            data = soup.findAll('div', items_list_div)
            items = list(map(lambda d: self.get_item_format_1(d), data))
            return items

        else:
            print('format 2')
            items_list_div = self.config_data['ITEM_DETAILS_FORMAT_2']['ITEM_LIST']
            data = soup.findAll('div', items_list_div)
            items = list(map(lambda d: self.get_item_format_2(d), data))
            return items

    def get_items_on_multiple_pages(self):
        items = []
        elements = self.driver.find_elements(By.CLASS_NAME, "index-module_item__RFluh")
        if elements:
            button = elements[-1].find_element(By.TAG_NAME, "button")
            while button.is_enabled():
                button.click()
                time.sleep(10)
                items += self.get_items_on_page()
                button = (self.driver.find_elements(By.CLASS_NAME, "index-module_item__RFluh")[-1]
                          .find_element(By.TAG_NAME, "button"))
        return items

    def get_collection_items(self, link) -> List[Item]:
        self.driver.get(link)
        time.sleep(10)
        items = self.get_items_on_page()
        items += self.get_items_on_multiple_pages()
        return items



