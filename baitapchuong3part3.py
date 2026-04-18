class NhanVien:
    LUONG_MAX = 20000000.0 
    def __init__(self, tenNhanVien, luongCoBan=0.0, heSoluong=1.0):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = float(luongCoBan)
        self.heSoluong = float(heSoluong)

    def get_tenNhanVien(self):
        return self.tenNhanVien
    def set_tenNhanVien(self, value):
        self.tenNhanVien = value
    def get_luongCoBan(self):
        return self.luongCoBan
    def set_luongCoBan(self, value):
        self.luongCoBan = value
    def get_heSoLuong(self):
        return self.heSoluong
    def set_heSoLuong(self, value):
        self.heSoLuong = value
    def tinhLuong(self):
        return self.luongCoBan * self.heSoluong

    def inTTin(self):
        print(f"Tên nhân viên: {self.get_tenNhanVien()}")
        # Sửa dấu , thành dấu : ở đây
        print(f"Lương cơ bản: {self.get_luongCoBan():,.0f}") 
        print(f"Hệ số lương: {self.get_heSoLuong()}")
        print(f"Lương thực nhận: {self.tinhLuong():,.0f}")

    def tangLuong(self, delta):
        luong_moi = self.luongCoBan * (self.heSoluong + delta)
        
        if luong_moi > NhanVien.LUONG_MAX:
            print("-> Lương mới vượt quá lương lớn nhất. Không thể tăng lương")
            return False
        else:
            self.heSoluong += delta
            print(f"-> Tăng lương thành công! Lương thực nhận mới: {self.tinhLuong():,.0f}")
            return True

nv1 = NhanVien("Do Minh Duc", 5000000.0, 2.0)
nv1.inTTin()

print("\nTĂNG LƯƠNG LẦN 1 ")
ket_qua_1 = nv1.tangLuong(0.5)
print(f"Kết quả trả về của hàm: {ket_qua_1}")

print("\n TĂNG LƯƠNG LẦN 2 ")
ket_qua_2 = nv1.tangLuong(20.0)
print(f"Kết quả trả về của hàm: {ket_qua_2}")