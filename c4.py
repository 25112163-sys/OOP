class LineSeparator:
    def __init__(self, sep):
        if len(args) ==0:
            self._d1 = point(0,5)
            self._d2 = point(1,0)
        if len(args) == 2:
            if isinstance(args[0], point) and isinstance(args[1], point):
            self._d1 = args[0]
            self._d2 = args[1]
        if len(args) == 4:
            if all(isinstance(arg[0], int):):
                self._d1 = point(args[0], args[1])
                self._d2 = point(args[2], args[3])
        if len(args) == 1:
            if isinstance(args[0], LineSeparator):
                self._d1 = copy.deepcopy(args[0]._d1)
                self._d2 = copy.deepcopy(args[0]._d2)
    def __str__(self):
        return f"(%d, %d) -> (%d, %d)" % (self._d1.x, self._d1.y, self._d2.x, self._d2.y)
    
    def get01(self):
        return self._d1
    def get02(self):
        return self._d2
    def set0102(self, point1, point2):
        self._d1 = point1
        self._d2 = point2

if name == "__main__":
    line1 = LineSeparator()
    print(line1)
    
    line2 = LineSeparator(point(2, 3), point(4, 5))
    print(line2)
    
    line3 = LineSeparator(-3, -4, -5, -6)
    print(line3)
    
    line4 = LineSeparator(line2)
    print(line4)

print(line1.get01())
print(line1.get02())