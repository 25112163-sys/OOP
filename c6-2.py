import os
from abc import ABC, abstractmethod
class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Tuổi {tuoi} không hợp lệ (phải từ 18-65)")

class CapBacKhongHopLe(Exception):
    def __init__(self, value):
        super().__init__(f"Cấp bậc {value} không hợp lệ (phải từ 1-10)")
class CanBo(ABC):
    def __init__(self, ten, tuoi, dia_chi, gioi_tinh):
        self.ten = ten
        self.tuoi = tuoi  # Sẽ gọi setter để kiểm tra
        self.dia_chi = dia_chi
        self.gioi_tinh = gioi_tinh

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, v):
        if not (18 <= v <= 65):
            raise TuoiKhongHopLe(v)
        self._tuoi = v

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ten} | {self.tuoi}t | {self.gioi_tinh} | {self.dia_chi}"
    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.ten)}, {self.tuoi}, {repr(self.dia_chi)}, {repr(self.gioi_tinh)})"

    def __eq__(self, o):
        if not isinstance(o, CanBo): return False
        return self.ten == o.ten and self.tuoi == o.tuoi

    def __lt__(self, o):
        if not isinstance(o, CanBo): return False
        return self.ten < o.ten
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, dia_chi, gioi_tinh, cap_bac):
        super().__init__(ten, tuoi, dia_chi, gioi_tinh)
        self.cap_bac = cap_bac

    @property
    def cap_bac(self):
        return self._cap_bac

    @cap_bac.setter
    def cap_bac(self, v):
        if not (1 <= v <= 10):
            raise CapBacKhongHopLe(v)
        self._cap_bac = v

    def mo_ta(self):
        return f"Công nhân bậc {self.cap_bac}"

    def __str__(self):
        return f"[Công nhân] {super().__str__()} | Bậc: {self.cap_bac}"

    def __repr__(self):
        return f"CongNhan({repr(self.ten)}, {self.tuoi}, {repr(self.dia_chi)}, {repr(self.gioi_tinh)}, {self.cap_bac})"

class KySu(CanBo):
    def __init__(self, ten, tuoi, dia_chi, gioi_tinh, nganh_dao_tao):
        super().__init__(ten, tuoi, dia_chi, gioi_tinh)
        self.nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"Kỹ sư ngành {self.nganh_dao_tao}"

    def __str__(self):
        return f"[Kỹ sư]    {super().__str__()} | Ngành: {self.nganh_dao_tao}"

    def __repr__(self):
        return f"KySu({repr(self.ten)}, {self.tuoi}, {repr(self.dia_chi)}, {repr(self.gioi_tinh)}, {repr(self.nganh_dao_tao)})"

class NhanVien(CanBo):
    def __init__(self, ten, tuoi, dia_chi, gioi_tinh, cong_viec):
        super().__init__(ten, tuoi, dia_chi, gioi_tinh)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên: {self.cong_viec}"

    def __str__(self):
        return f"[Nhân viên] {super().__str__()} | CV: {self.cong_viec}"

    def __repr__(self):
        return f"NhanVien({repr(self.ten)}, {self.tuoi}, {repr(self.dia_chi)}, {repr(self.gioi_tinh)}, {repr(self.cong_viec)})"

class QuanLy:
    def __init__(self):
        self.danh_sach = []

    def add_can_bo(self, cb):
        if cb in self.danh_sach:
            print("Cán bộ này đã tồn tại trong danh sách!")
        else:
            self.danh_sach.append(cb)
            print("Thêm cán bộ thành công!")

    def hien_thi(self):
        if not self.danh_sach:
            print("\n📭 Danh sách đang trống.")
        else:
            print("\n--- DANH SÁCH CÁN BỘ (Sắp xếp A-Z) ---")
            for cb in sorted(self.danh_sach):
                print(cb)

    def tim_kiem(self, ten):
        kq = [cb for cb in self.danh_sach if ten.lower() in cb.ten.lower()]
        if kq:
            print(f"\n Tìm thấy {len(kq)} kết quả:")
            for cb in kq: print(f" -> {cb}")
        else:
            print(f"Không tìm thấy ai có tên '{ten}'")

    def ghi_file(self, filename="data.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.danh_sach:
                f.write(repr(cb) + "\n")
        print(f"Đã lưu dữ liệu vào '{filename}'")

    def doc_file(self, filename="data.txt"):
        if not os.path.exists(filename):
            print(" File không tồn tại.")
            return
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.danh_sach = [eval(line.strip()) for line in f if line.strip()]
            print(f" Đã tải dữ liệu từ '{filename}'")
        except Exception as e:
            print(f" Lỗi khi đọc file: {e}")

    def menu(self):
        while True:
            print("\n" + "—"*30 + "\n  HỆ THỐNG QUẢN LÝ CÁN BỘ\n" + "—"*30)
            print("1. Thêm cán bộ\n2. Hiển thị danh sách\n3. Tìm kiếm\n4. Lưu file\n5. Đọc file\n0. Thoát")
            choice = input("Chọn chức năng: ")

            if choice == "1":
                try:
                    loai = input("Loại (CN/KS/NV): ").lower()
                    ten = input("Tên: ")
                    tuoi = int(input("Tuổi: "))
                    dc = input("Địa chỉ: ")
                    gt = input("Giới tính: ")
                    
                    if loai == "cn":
                        bac = int(input("Cấp bậc (1-10): "))
                        self.add_can_bo(CongNhan(ten, tuoi, dc, gt, bac))
                    elif loai == "ks":
                        nganh = input("Ngành đào tạo: ")
                        self.add_can_bo(KySu(ten, tuoi, dc, gt, nganh))
                    elif loai == "nv":
                        cv = input("Công việc: ")
                        self.add_can_bo(NhanVien(ten, tuoi, dc, gt, cv))
                    else: print(" Loại không hợp lệ.")
                except Exception as e: print(f" Lỗi: {e}")

            elif choice == "2": self.hien_thi()
            elif choice == "3": self.tim_kiem(input("Nhập tên: "))
            elif choice == "4": self.ghi_file()
            elif choice == "5": self.doc_file()
            elif choice == "0": break
if __name__ == "__main__":
    ql = QuanLy()
    ql.menu()