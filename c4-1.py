class NhanVien:
    LUONG_MAX = 10000000
    def __init__(self,tenNhanVien="",luongCoBan=0,heSoLuong=0.0):
        self.__tenNhanVien=tenNhanVien
        self.__luongCoBan=luongCoBan
        self.__heSoLuong=heSoLuong
    def set__tenNhanVien(self,tenNhanVien):
        self.__tenNhanVien=tenNhanVien
    def set__luongCoBan(self,luongCoBan):
        self.__luongCoBan=luongCoBan
    def set__heSoLuong(self,heSoLuong):
        self.__heSoLuong=heSoLuong
    def get__tenNhanVien(self):
        return self.__tenNhanVien
    def get__luongCoBan(self):
        return self.__luongCoBan
    def get__heSoLuong(self):
        return self.__heSoLuong
    def tinhLuong(self):
        luongThucNhan=self.get__luongCoBan()*self.get__heSoLuong()
        return luongThucNhan
    def inTTin(self):
        print(f'Nhân viên: {self.get__tenNhanVien()}')
        print(f'Lương thực nhận = {self.get__luongCoBan()} x {self.get__heSoLuong()} = {self.tinhLuong()}')
    def tangLuong(self,hesotangthem=0.0):
        hesotangthem=float(input('Nhập hệ số lương tăng thêm: '))
        luongMoi=self.get__luongCoBan()*(self.__heSoLuong+hesotangthem)
        if (luongMoi)>self.LUONG_MAX:
            print('Lương quá cao. Không thể tăng lương')
            return False
        else:
            print('Tăng lương thành công.')
            self.set__heSoLuong(self.__heSoLuong+hesotangthem)
            print(f'Lương mới= {self.get__luongCoBan()} x {self.get__heSoLuong()}= {luongMoi}')
         
nv1=NhanVien("Sayu",100000,2.5)
nv1.inTTin()
nv1.tangLuong()
nv1.set__heSoLuong(3.6)
nv1.inTTin()