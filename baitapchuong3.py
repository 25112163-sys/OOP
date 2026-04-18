class Dog:
    def __init__(self,name ,colour , giong, emotion):
        self.name= name
        self.colour = colour
        self.giong = giong
        self.emotion = emotion
        self.hunger_level = 50
    def sua(self):
        print(f" con chó {self.name} ({self.colour}) ({self.giong}) sủa: Gâu gâu! Cảm xúc hiện tại: {self.emotion}.")

    def vay_duoi(self):
        self.cam_xuc = "Vui vẻ"
        print(f" con chó {self.name} đang vẫy đuôi. Cảm xúc chuyển thành: {self.cam_xuc}.")

    def eat(self,food):
        if self.hunger_level > 0:
            print(f"con chó {self.name} đang ăn {food}...")
            self.hunger_level -= 20
            if self.hunger_level < 0: self.hunger_level = 0
            print(f"   -> Đã ăn xong! Mức độ đói giảm còn: {self.hunger_level}/100.")
        else:
            print(f"con chó{self.name} không muốn ăn thêm")

    def run(self):
        print(f"con chó {self.name} đang chạy nhảy tung tăng")
        self.hunger_level += 10
        print(f"  -> Chạy mệt nên mức độ đói tăng lên: {self.hunger_level}/100.")
    
print("\n" + "="*40)
print("ĐỐI TƯỢNG CON CHÓ")
print("="*40)
dog1= Dog("Mộ Xum Xuê","màu Vàng","Giống Cao Bằng","Vui vẻ")
dog1.sua()
dog1.vay_duoi()
dog1.run()
dog1.eat("bã mía")


class Car:
    def __str__(self):
        return f"Xe {self.hang}, màu {self.colour}, giá {self.price}"
    def __init__(self, hang, size ,colour, price):
        self.hang = hang
        self.size = size
        self.colour = colour
        self.price = price
        self.current_speed = 0 
        self.running= False

    def speedup(self, speedup):
        self.running = True
        self.current_speed += speedup
        print(f"Xe {self.hang} tăng tốc. Tốc độ hiện tại: {self.current_speed} km/h.")

    def deceleration(self, deceleration):
        if self.current_speed > 0:
            self.current_speed -= deceleration
            if self.current_speed <= 0:
                self.current_speed = 0
                self.running = False
            print(f"Xe {self.hang} giảm tốc. Tốc độ hiện tại: {self.current_speed} km/h.")
        else:
            print(f"Xe {self.hang} đã dừng hẳn, không thể giảm tốc thêm.")

    def crash(self):
        if self.current_speed > 0:
            print(f"RẦM! Xe {self.hang} va chạm khi đang đi với tốc độ {self.current_speed} km/h!")
            self.current_speed = 0
            self.running = False
        else:
            print(f"Xe {self.hang} đang đỗ mà tự nhiên bị đâm trúng!")
print("\n" + "="*40)
print("ĐỐI TƯỢNG Ô TÔ")
print("="*40)
Xe1= Car("lamborghini","Lớn","vàng","43.990.000.000 VNĐ")
print(Xe1)
Xe1. speedup(40)
Xe1. speedup(20)
Xe1. deceleration(10)
Xe1. crash()

class Account:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du=0):
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self._so_du = so_du
    def gui(self, so_tien):
        if so_tien > 0:
            self._so_du += so_tien
            print(f"Nạp thành công {so_tien:,.0f} VNĐ. Số dư hiện tại: {self._so_du:,.0f} VNĐ.")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def rut(self, so_tien):
        if so_tien <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        elif so_tien > self._so_du:
            print(f"Số dư không đủ! (Bạn muốn rút {so_tien:,.0f} nhưng chỉ có {self._so_du:,.0f})")
        else:
            self._so_du -= so_tien
            print(f"[-] Rút thành công {so_tien:,.0f} VNĐ. Số dư còn lại: {self._so_du:,.0f} VNĐ.")

    def kiem_tra_so_du(self):
        print(f"Tài khoản: {self.so_tk} | Chủ TK: {self.ten_tk} | Ngân hàng: {self.ngan_hang}")
        print(f"Số dư hiện tại: {self._so_du:,.0f} VNĐ.")

print("\n" + "="*40)
print("ĐỐI TƯỢNG TÀI KHOẢN")
print("="*40)
my_account = Account("Do Minh Duc", "0337581095", "Techcombank", 1000000)
my_account.kiem_tra_so_du()
print("-" * 30)
my_account.gui(500000)
my_account.rut(2000000)
my_account.rut(1200000)