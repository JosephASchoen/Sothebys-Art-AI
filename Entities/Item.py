class Item:
    def __init__(self, author, title, estimate_price, price_sold):
        self.author = author
        self.title = title
        self.estimate_price = estimate_price
        self.price_sold = price_sold

    def print(self):
        print('\t', '\t', 'author:', self.author)
        print('\t', '\t', 'title:', self.title)
        print('\t', '\t', 'estimated price:', self.estimate_price)
        print('\t', '\t', 'sold_price:', self.price_sold)
