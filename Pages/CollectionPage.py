from Pages import ItemsPage
from Entities.Collection import Collection
import Util


class CollectionPage(object):
    def __init__(self, driver, config_data):
        self.driver = driver
        self.config_data = config_data

    def get_collection(self, data):
        category = Util.get_text(data, 'div', 'Card-category')
        title = Util.get_text(data, 'div', 'Card-title')
        details = Util.get_text(data, 'div', 'Card-details')
        price = Util.get_text(data, 'div', 'Card-salePrice')
        link = data.find('a', class_='Card-info-container')['href']

        items_page = ItemsPage.ItemsPage(self.driver, self.config_data)
        items = items_page.get_collection_items(link)

        collection = Collection(category, title, details, price, link, items)
        collection.print()
        print('\n')
        return collection
