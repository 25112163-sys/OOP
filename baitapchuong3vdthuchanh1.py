import math 
diem = []
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Điểm vừa tạo: (%d, %d)' % (self.x, self.y))
    def printpoint(self):
        print('(%d, %d)' % (self.x, self.y))
        
    def inputpoint(self):
        self.x = int(input('Nhập x: '))
        self.y = int(input('Nhập y: '))
    def doixung(self):
        return Point(-self.x, -self.y)    
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)   
O=Point(0,0)
p1 = Point(int(input('Nhập điểm x: ')), int(input('Nhập điểm y: ')))
diem.append(p1) 
p2 = Point(int(input('Nhập điểm x: ')), int(input('Nhập điểm y: ')))
diem.append(p2)
p3=p2.doixung()
diem.append(p3)
print(diem)
khoangcach=p2.distance(O)
print('Khoảng cách từ điểm p2 đến gốc tọa độ là: %.2f' % khoangcach)
khoangcach2=p1.distance(p2)
print('Khoảng cách từ điểm p1 đến điểm p2 là: %.2f' % khoangcach2)