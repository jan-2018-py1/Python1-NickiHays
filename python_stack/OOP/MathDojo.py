class MathDojo(object):
    def __init__(self):
        self.number = 0
    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.number += value
            else:
                self.number += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.number -= value
            else:
                self.number -= arg
        return self


md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).number

md2 = MathDojo()
print md2.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).number

md3 = MathDojo()
print md3.add(5,(10,7),6).subtract(3,[2,4],(3,5)).number

