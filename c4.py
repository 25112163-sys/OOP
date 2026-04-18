import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class LineSeparator:
    def __init__(self, *args):
        if len(args) == 0:
            self._d1 = Point(0, 5)
            self._d2 = Point(1, 0)

        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self._d1 = args[0]
                self._d2 = args[1]
            else:
                raise TypeError("Phải truyền 2 đối tượng Point")

        elif len(args) == 4:
            if all(isinstance(arg, int) for arg in args):
                self._d1 = Point(args[0], args[1])
                self._d2 = Point(args[2], args[3])
            else:
                raise TypeError("Phải là 4 số nguyên")

        elif len(args) == 1:
            if isinstance(args[0], LineSeparator):
                self._d1 = copy.deepcopy(args[0]._d1)
                self._d2 = copy.deepcopy(args[0]._d2)
            else:
                raise TypeError("Phải là LineSeparator")

        else:
            raise ValueError("Sai số lượng tham số")

    def __str__(self):
        return f"{self._d1} -> {self._d2}"

    def get01(self):
        return self._d1

    def get02(self):
        return self._d2

    def set0102(self, point1, point2):
        if isinstance(point1, Point) and isinstance(point2, Point):
            self._d1 = point1
            self._d2 = point2
        else:
            raise TypeError("Phải là Point")


# --- Test ---
if __name__ == "__main__":
    line1 = LineSeparator()
    print(line1)

    line2 = LineSeparator(Point(2, 3), Point(4, 5))
    print(line2)

    line3 = LineSeparator(-3, -4, -5, -6)
    print(line3)

    line4 = LineSeparator(line2)
    print(line4)

    print(line1.get01())
    print(line1.get02())