import math

# Custom Exception
class MauSoBangKhong(Exception):
    def __init__(self):
        super().__init__("Mẫu số không được bằng 0")


class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
        self._toi_gian()  # tự động tối giản

    # --- Property ---
    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self, value):
        self.__tu = value

    @property
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau = value

    # --- Tối giản ---
    def _toi_gian(self):
        u = math.gcd(self.tu, self.mau)
        if u != 0:
            self.__tu //= u
            self.__mau //= u
        if self.__mau < 0:
            self.__tu = -self.__tu
            self.__mau = -self.__mau

    def is_toi_gian(self):
        return math.gcd(self.tu, self.mau) == 1

    # --- Toán tử ---
    def __add__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return PhanSo(
            self.tu * other.mau + other.tu * self.mau,
            self.mau * other.mau
        )

    def __sub__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return PhanSo(
            self.tu * other.mau - other.tu * self.mau,
            self.mau * other.mau
        )

    def __mul__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return PhanSo(
            self.tu * other.tu,
            self.mau * other.mau
        )

    def __truediv__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
        return PhanSo(
            self.tu * other.mau,
            self.mau * other.tu
        )

    # --- So sánh ---
    def __eq__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu * other.mau == other.tu * self.mau

    def __lt__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu * other.mau < other.tu * self.mau

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu * other.mau > other.tu * self.mau

    def __ge__(self, other):
        return self > other or self == other

    # --- Hiển thị ---
    def __str__(self):
        return f"{self.tu}" if self.mau == 1 else f"{self.tu}/{self.mau}"

    def __repr__(self):
        return f"PhanSo({self.tu}, {self.mau})"


# --- Chương trình chính ---
def main():
    danh_sach = []
    print("Nhập danh sách phân số (nhập 'q' để dừng)")

    while True:
        try:
            s = input("\nNhập tử số: ")
            if s.lower() == 'q':
                break

            tu = int(s)
            mau = int(input("Nhập mẫu số: "))

            ps = PhanSo(tu, mau)
            danh_sach.append(ps)

        except MauSoBangKhong as e:
            print("Lỗi:", e)
        except ValueError:
            print("Lỗi: nhập số nguyên!")

    if danh_sach:
        print("\n--- Danh sách phân số ---")
        print(" | ".join(str(ps) for ps in danh_sach))

        danh_sach.sort()

        print("\n--- Sau khi sắp xếp ---")
        print(" | ".join(str(ps) for ps in danh_sach))
    else:
        print("Danh sách rỗng")


if __name__ == "__main__":
    main()