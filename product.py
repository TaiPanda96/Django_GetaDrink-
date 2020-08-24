class Product(object):
    def __init__(self,product,price):
        self.product  = product 
        self.price    = price 
        self.attributes = dict()
    
    def to_map(self):
        data = self.attributes
        if self.product:
           data['product']   = self.product
        
        if self.price:
           data['price']     = self.price

        return data