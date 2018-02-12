class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 90
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "I have {} health".format(self.health)


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self). __init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
d = Dog("Charlie")
d.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self
c = Dragon("Eragon")
c.walk().walk().run().fly().display_health()

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.health = 160
    def purr(self):
        self.health += 15
        return self
x = Cat("Taco")
x.walk().run().fly().pet().display_health()

