class CanBo:
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi):
        self.ten = ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        
    def loai_CanBo(self):
        return "Cán bộ"

    def hien_thi(self):
        print(f'Tên: {self.ten}')
        print(f'Tuổi: {self.tuoi}')
        print(f'Giới tính: {self.gioi_tinh}')
        print(f'Địa chỉ: {self.dia_chi}')
        
    def __str__(self):
        return f'{self.loai_CanBo()} - Tên: {self.ten}, Tuổi: {self.tuoi}, Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}'
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        if bac < 1 or bac > 10:
            raise ValueError("Bậc phải từ 1 đến 10")
        self.bac = bac
        
    def loai_CanBo(self):  
        return "Công nhân"
        
    def hien_thi(self):
        print("\n--- Thông tin Công nhân ---")
        super().hien_thi()
        print(f'Bậc: {self.bac}')


class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
        
    def loai_CanBo(self):
        return "Kỹ sư"
        
    def hien_thi(self):
        print("\n--- Thông tin Kỹ sư ---")
        super().hien_thi()
        print(f'Ngành đào tạo: {self.nganh_dao_tao}')


class NhanVien(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
        
    def loai_CanBo(self):
        return "Nhân viên"
        
    def hien_thi(self):
        print("\n--- Thông tin Nhân viên ---")
        super().hien_thi()
        print(f'Công việc: {self.cong_viec}')

class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []
        
    def them_moi(self):
        print("\n--- Thêm mới cán bộ ---")
        loai = input("Nhập loại cán bộ (1: Công nhân, 2: Kỹ sư, 3: Nhân viên): ")
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        gioi_tinh = input("Nhập giới tính: ")
        dia_chi = input("Nhập địa chỉ: ")
        
        if loai == '1':
            bac = int(input("Nhập bậc (1-10): "))
            can_bo = CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)
        elif loai == '2':
            nganh_dao_tao = input("Nhập ngành đào tạo: ")
            can_bo = KySu(ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao)
        elif loai == '3':
            cong_viec = input("Nhập công việc: ")
            can_bo = NhanVien(ten, tuoi, gioi_tinh, dia_chi, cong_viec)
        else:
            print("Loại cán bộ không hợp lệ.")
            return
        
        self.danh_sach_can_bo.append(can_bo)
        print("Thêm cán bộ thành công!")
    def tim_kiem(self):
        print("\n--- Tìm kiếm cán bộ ---")
        ten = input("Nhập tên cán bộ cần tìm: ")
        found = False
        for can_bo in self.danh_sach_can_bo:
            if can_bo.ten.lower() == ten.lower():
                can_bo.hien_thi()
                found = True
                break
        if not found:
            print("Không tìm thấy cán bộ với tên đã nhập.")
        else:
            print("Tìm kiếm thành công!")
            for can_bo in self.danh_sach_can_bo:
                can_bo.hien_thi()
    def hien_thi_danh_sach(self):
        print("\n--- Danh sách cán bộ ---")
        if not self.danh_sach_can_bo:
            print("Danh sách cán bộ trống.")
        else:
            for can_bo in self.danh_sach_can_bo:
                can_bo.hien_thi()
    def chay(self):
        while True:
            print("\n--- Quản lý cán bộ ---")
            print("1. Thêm mới cán bộ")
            print("2. Tìm kiếm cán bộ")
            print("3. Hiển thị danh sách cán bộ")
            print("4. Thoát")
            lua_chon = input("Nhập lựa chọn: ")
            if lua_chon == '1':
                self.them_moi()
            elif lua_chon == '2':
                self.tim_kiem()
            elif lua_chon == '3':
                self.hien_thi_danh_sach()
            elif lua_chon == '4':
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    qlcb = QLCB()
    qlcb.chay()