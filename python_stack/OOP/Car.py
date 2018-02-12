# price
# speed
# fuel (full, not full, empty)
# mileage
# price > 10000 tax = 15% else 12%
# display_all()


class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def display_all(self):
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        print "Price: ${}".format(self.price)
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax", self.tax 
        return self

car1 = Car(3000, '20mph', 'Not Full', '85mpg')
car2 = Car(1500, '25mph', 'Full', '30mpg')
car3 = Car(20000, '50mph', 'Almost Full', '95mpg')
car4 = Car(15000, '35mph', 'Half Full', '50mpg')
car5 = Car(6000, '30mph', 'Empty', '60mpg')
car6 = Car(50000, '60mph', 'Full', '100mpg')

print "Car # 1:"
car1.display_all()

print "Car # 2:"
car2.display_all()

print "Car # 3:"
car3.display_all()

print "Car # 4:"
car4.display_all()

print "Car # 5:"
car5.display_all()

print "Car # 6:"
car6.display_all()