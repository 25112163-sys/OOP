import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class LineSegment:
    # 1. Constructor mặc định
    def __init__(self, *args):
        if len(args) == 0:
            # mặc định
            self.d1 = Point(8, 5)
            self.d2 = Point(1, 0)

        elif len(args) == 2 and all(isinstance(p, Point) for p in args):
            # 2 Point
            self.d1 = args[0]
            self.d2 = args[1]

        elif len(args) == 4:
            # 4 số int
            self.d1 = Point(args[0], args[1])
            self.d2 = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            # copy constructor
            s = args[0]
            self.d1 = Point(s.d1.x, s.d1.y)
            self.d2 = Point(s.d2.x, s.d2.y)

        else:
            raise ValueError("Invalid arguments")

    def display(self):
        print(f"LineSegment [({self.d1.x}, {self.d1.y}) to ({self.d2.x}, {self.d2.y})]")