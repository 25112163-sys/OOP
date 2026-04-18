class SieuNhan:
    def __init__(self, name,weapon,color):
        self.name = name
        self.weapon = weapon
        self.color = color
    def __str__(self):
        return f"SieuNhan(name={self.name}, weapon={self.weapon}, color={self.color})"
    
sieu_nhan_A = SieuNhan("SieuNhanA", "Kiếm", "Đỏ")
sieu_nhan_B = SieuNhan("SieuNhanB", "Khiên", "Xanh")
print(sieu_nhan_A)
print(sieu_nhan_B)