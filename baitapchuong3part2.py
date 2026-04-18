class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def contains_point(self, p):
        distance = ((self.center.x - p.x) ** 2 + (self.center.y - p.y) ** 2) ** 0.5
        return distance <= self.r  

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_corners(self):
        # Lấy danh sách 4 góc của hình chữ nhật
        return [ #kiểu list để chứa 4 góc của hình chữ nhật
            self.top_left,
            Point(self.bottom_right.x, self.top_left.y),
            self.bottom_right,
            Point(self.top_left.x, self.bottom_right.y)
        ]

    def is_inside_circle(self, c):
        for corner in self.get_corners():
            if not c.contains_point(corner):
                return False 
        return True

    def overlaps_circle(self, c):
        closest_x = max(self.top_left.x, min(c.center.x, self.bottom_right.x))
        closest_y = max(self.top_left.y, min(c.center.y, self.bottom_right.y))
        
        distance = ((c.center.x - closest_x) ** 2 + (c.center.y - closest_y) ** 2) ** 0.5
        return distance <= c.r

print("--- TẠO HÌNH TRÒN ---")
cx = int(input('Nhập x tâm: '))
cy = int(input('Nhập y tâm: '))
r = int(input('Nhập bán kính: '))
my_circle = Circle(Point(cx, cy), r)

print("\n--- TẠO HÌNH CHỮ NHẬT ---")
tx = int(input('Nhập x góc trên trái: '))
ty = int(input('Nhập y góc trên trái: '))
bx = int(input('Nhập x góc dưới phải: '))
by = int(input('Nhập y góc dưới phải: '))
my_rect = Rectangle(Point(tx, ty), Point(bx, by))

print("\n--- KẾT QUẢ ---")
if my_rect.is_inside_circle(my_circle):
    print("-> Hình chữ nhật nằm hoàn toàn trong hình tròn")
elif my_rect.overlaps_circle(my_circle):
    print("-> Hình chữ nhật có giao/chồng lấp với hình tròn")
else:
    print("-> Hình chữ nhật nằm hoàn toàn ngoài hình tròn")