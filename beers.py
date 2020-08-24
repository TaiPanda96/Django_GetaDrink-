class Beer(object):
    def __init__(self,product,category, price, volume):
        self.product  = product 
        self.category = category
        self.price    = price 
        self.volume   = volume
        self.attributes = dict()
    
    def to_map(self):
        data = self.attributes
        if self.product:
           data['product']   = self.product
        
        if self.category:
           data['category']  = self.category
        
        if self.price:
           data['price']     = self.price

        if self.volume:
           data['volume']    = self.volume
        
        return data
    
    # def __str__(self):
    #     data = self.to_map()
    #     return data



if __name__ == "__main__":
    lager = Beer('Henderson Ambers','Amber Lagers',6.25,'300ml').to_map()
    ipa   = Beer('Society of Beer Drinking Ladies','IPA',5.25,'275ml').to_map()
    ale   = Beer('Blanche de Tremblay','Wheat Ale',4.25,'300ml').to_map()
    print(lager,ipa,ale)