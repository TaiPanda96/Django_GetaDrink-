class Product(object):
    def __init__(self,product,price,category=None):
        self.product  = product 
        self.price    = price 
        self.category = category
        self.attributes = dict()
    
    def to_map(self):
        data = self.attributes
        if self.product:
           data['product']   = self.product
        
        if self.price:
           data['price']     = self.price

        if self.category:
           data['category']  = self.category

        return data


