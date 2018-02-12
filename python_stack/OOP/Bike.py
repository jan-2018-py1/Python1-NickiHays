# price
# max_speed
# miles
# use init to specifiy price & max speed of each instance ex bike1=bike(200, "25mph")
# initial miles se to 0 whenever new instance created
# display() - display price, max speed, & miles
# ride() - display "Riding" on the screen and increase total miles by 10
# reverse() - display "Reversing" on screen and decrease mile by 5
# bike1 ride 3x, reverse 1x, & then display info
# bike2 ride 2x, reverse 2x, & then display info
# bike3 reverse 3x & then display


class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display(self):
        print "Price: ${}".format(self.price)
        print "Max Speed:", self.max_speed
        print "Total Miles:", self.miles, 'miles'
        return self

    def ride(self):
        miles_ridden = self.miles = self.miles + 10
        print "Riding"
        print "Total Miles:", miles_ridden
        return self

    def reverse(self):
        miles_ridden = self.miles =  self.miles - 5
        print "Reversing"
        print "Total Miles:", miles_ridden
        return self

bike1 = Bike(300, '25mph')
bike2 = Bike(1000, '35mph')
bike3 = Bike(2000, '50mph')

print "Bike # 1:"
bike1.ride().ride().ride().reverse().display()

print "Bike # 2:"
bike2.ride().ride().reverse().reverse().display()

print "Bike # 3:"
bike3.reverse().reverse().reverse().display()
