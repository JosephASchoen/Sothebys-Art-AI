import Util
from bs4 import BeautifulSoup
from Pages.CollectionPage import CollectionPage
import time
from typing import List
from Entities.Collection import Collection


class ResultsPage(object):
    def __init__(self, driver, config_data):
        self.driver = driver
        self.config_data = config_data

    def get_page_results(self, _url) -> List[Collection]:
        print(_url)
        self.driver.get(_url)
        time.sleep(self.config_data['WAIT_TIME_SMALL'])
        html = self.driver.page_source
        soup = BeautifulSoup(html, parser='html.parser', features="lxml")
        data = soup.findAll("li", class_='SearchModule-results-item')
        collections = list(map(lambda n: CollectionPage(self.driver, self.config_data).get_collection(n), data))
        return collections
