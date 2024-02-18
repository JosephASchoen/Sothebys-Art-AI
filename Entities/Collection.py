from typing import List
from Entities.Item import Item
class Collection:
    def __init__(self, category: str, title: str, details: str, price: str, link: str, items: List[Item]):
        self.category = category
        self.title = title
        self.details = details
        self.price = price
        self.link = link
        self.items = items

    def to_dict(self):
        collection_dict = {
            "collection_category": self.category,
            "collection_title": self.title,
            "collection_details": self.details,
            "collection_price": self.price,
        }

        if self.items:
            item_dicts = list(
                map(
                    lambda item: item.to_dict().update(collection_dict),
                    self.items
                )
            )
            return item_dicts

        return collection_dict

    def print(self):
        print('\t', 'category:', self.category)
        print('\t', 'title:', self.title)
        print('\t', 'details:', self.details)
        print('\t', 'price:', self.price)
        print('\t', 'link:', self.link)

        if not self.items:
            print('\t no items')
        else:
            for item in self.items:
                item.print()