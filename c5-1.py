class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def getMaHang(self):
        return self.ma_hang
    def getTenHang(self):
        return self.ten_hang
    def getNhaSX(self):
        return self.nha_sx

    def hien_thi(self):
        print(f'Mã hàng: {self.ma_hang}')
        print(f'Tên hàng: {self.ten_hang}')
        print(f'Nhà sản xuất: {self.nha_sx}')
        print(f'Giá: {self.gia} VND')
class HangDienMay(HangHoa):
    def __init__(self, tg_baohanh, dien_ap, cong_suat, ma_hang, ten_hang, nha_sx, gia):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
    def hien_thi(self):
        print(f'\n--- Thông tin hàng điện máy ---')
        super().hien_thi()
        print(f'Thời gian bảo hành: {self.tg_baohanh} tháng')
        print(f'Điện áp: {self.dien_ap} V')
        print(f'Công suất: {self.cong_suat} W')


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def hien_thi(self):
        print(f'\n--- Thông tin hàng sành sứ ---')
        super().hien_thi()
        print(f'Loại nguyên liệu: {self.loai_nguyenlieu}')


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def hien_thi(self):
        print(f'\n--- Thông tin hàng thực phẩm ---')
        super().hien_thi()
        print(f'Ngày sản xuất: {self.ngay_sx}')
        print(f'Ngày hết hạn: {self.ngay_het_han}')

hang1 = HangDienMay(24, 220, 1500, 'DM001', 'Tủ lạnh', 'Samsung', 10000000)
hang1.hien_thi()

hang2 = HangSanhSu('CB0036', 'Bộ ấm chén', 'Bát Tràng', 500000, 'Sứ cao cấp')
hang2.hien_thi()

hang3 = HangThucPham('TP001', 'Sữa tươi', 'Vinamilk', 20000, '01/04/2024', '31/12/2024')
hang3.hien_thi()