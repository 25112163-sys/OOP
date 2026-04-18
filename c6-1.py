from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá {gia} không hợp lệ")
class MaHangTrungLap(Exception):
    def __init__(self, ma):
        self.ma = ma
        super().__init__(f"Mã hàng {ma} đã tồn tại")
class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self.__ma, self.__ten, self.__nsx = ma, ten, nsx
        self.gia = gia

    @property
    def ma_hang(self): return self.__ma
    @property
    def ten_hang(self): return self.__ten
    @property
    def gia(self): return self.__gia

    @gia.setter
    def gia(self, v):
        if v < 0:
            raise GiaKhongHopLe(v)
        self.__gia = v
        
    @abstractmethod
    def loai_hang(self): pass

    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma}"
                f" | {self.__ten} | {self.__gia:,.0f}đ")

    def __str__(self): return self.inTTin()
    def __repr__(self): return self.inTTin() 
    def __eq__(self, o): return self.__ma == o.ma_hang 
    def __lt__(self, o): return self.__gia < o.gia
    def __hash__(self): return hash(self.__ma)


class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
        super().__init__(ma, ten, nsx, gia)
        self.bh, self.dap, self.cs = bh, dap, cs

    def loai_hang(self): return "Điện máy"

    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | BH: {self.bh}th"
                f" | Đáp: {self.dap}V | CS: {self.cs}W")


class HangSanhSu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, nguyen_lieu):
        super().__init__(ma, ten, nsx, gia)
        self.nguyen_lieu = nguyen_lieu

    def loai_hang(self): return "Sành sứ"

    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | NL: {self.nguyen_lieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma, ten, nsx, gia, hsd):
        super().__init__(ma, ten, nsx, gia)
        self.hsd = hsd

    def loai_hang(self): return "Thực phẩm"

    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | HSD: {self.hsd}")

if __name__ == "__main__":
    ds = [
        HangDienMay("DM001", "Tủ lạnhh", "Samsung", 15000000, 24, 220, 500),
        HangSanhSu("SS001", "Bộ ấm chén", "Bát Tràng", 500000, "Sứ cao cấp"),
        HangThucPham("TP001", "Sữa tươi", "Vinamilk", 35000, "30/12/2024"),
        HangDienMay("DM002", "Tivi", "Sony", 12000000, 12, 220, 300)
    ]
    for sp in sorted(ds):
        print(sp)
    with open("kho.txt", "w", encoding="utf-8") as f:
        for sp in sorted(ds):
            f.write(repr(sp) + "\n")