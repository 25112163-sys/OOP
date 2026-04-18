import math
class point:
    """ represent a point in 2D geometry"""
    x = int
    y= int
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d,%d)"% (self.x,self.y)
    #phương thức nhập điểm từ bàn phím
    def read(self):
        self.x = int(input("x="))
        self.y = int(input("y="))
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d