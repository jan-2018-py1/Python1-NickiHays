class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
#        self.tax = 0

    def sell(self):
        self.status = "Sold"
        print self.status
        return self

    def addtax(self, percent):
        total_price = round(self.price * percent, 2) + self.price
        print total_price
        return self

    def returnItem(self, return_status):
        if return_status == "defective":
            self.price = 0
            self.status = "Defective"
        elif return_status == "like new":
            self.status = "For Sale"
        elif return_status == "opened":
            self.status = "Used"
            self.price = self.price * .8  #multiplying by .8 changes the price to already include the 20% discount
        return self

    def display(self):
        print "Item:", self.item_name
        print "Brand:", self.brand
        print "Price: ${}".format(self.price)
        print "Weight:", self.weight
        print "Status", self.status
        return self

a = Product(1800, 'Desktop', '3.5 lbs', 'HP')
b = Product(399, 'iPod', '.75 lbs', 'Apple')
c = Product(175, 'Baby Monitor', '.8 lbs', 'vtech')


a.addtax(.075).sell().returnItem('defective').display()
b.addtax(.068).sell().returnItem('like new').display()
c.addtax(.072).sell().returnItem('opened').display()