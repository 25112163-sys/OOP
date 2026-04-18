Luong_Co_Ban = 10000000

class nhanvien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da
        self.luong = Luong_Co_Ban * he_so_luong
        
    def tinh_luong(self):
        return Luong_Co_Ban * self.he_so_luong
        
    def hien_thi(self):
        print(f'Mã nhân viên: {self.ma_nv}')
        print(f'Họ tên: {self.ho_ten}')
        print(f'Năm sinh: {self.nam_sinh}')
        print(f'Giới tính: {self.gioi_tinh}')
        print(f'Địa chỉ: {self.dia_chi}')
        print(f'Hệ số lương: {self.he_so_luong}')
        print(f'Lương: {self.tinh_luong():,.0f} VND')
class CongTacVien(nhanvien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        if thoi_han_hd not in ['6 tháng', '1 năm', '2 năm']:
            print('Thời hạn hợp đồng không hợp lệ. Vui lòng chọn 6 tháng, 1 năm hoặc 2 năm.')
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld
        
    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap_ld
        
    def hien_thi(self):
        print("\n--- Thông tin Cộng tác viên ---")
        super().hien_thi()
        print(f'Thời hạn hợp đồng: {self.thoi_han_hd}')
        print(f'Phụ cấp lao động: {self.phu_cap_ld:,.0f} VND')

class NhanVienChinhThuc(nhanvien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri = vi_tri
        
    def hien_thi(self):
        print("\n--- Thông tin Nhân viên chính thức ---")
        super().hien_thi()
        print(f'Vị trí: {self.vi_tri}')

class TruongPhong(nhanvien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau_ql = ngay_bat_dau_ql
        self.phu_cap_ql = phu_cap_ql
        
    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap_ql
        
    def hien_thi(self):
        print("\n--- Thông tin Trưởng phòng ---")
        super().hien_thi()
        print(f'Ngày bắt đầu quản lý: {self.ngay_bat_dau_ql}')
        print(f'Phụ cấp quản lý: {self.phu_cap_ql:,.0f} VND')
ctv1 = CongTacVien('CTV001', 'Giang', 1998, 'Nam', 'Hà Nội', 2.5, 25000000, '1 năm', 500000)
ctv1.hien_thi()

nv1 = NhanVienChinhThuc('NV001', 'Quang', 2004, 'Nữ', 'Hà Nội', 3.0, 30000000, 'Kế toán')
nv1.hien_thi()

tp1 = TruongPhong('TP001', 'Thanh Hoa', 1980, 'Nữ', 'Đà Nẵng', 4.0, 40000000, '01/01/2020', 1000000)
tp1.hien_thi()