# Bài tập 1.2 - Think Python

# 1. Tính tổng số giây trong 42 phút 42 giây
phut = 42
giay = 42
tong_so_giay = (phut * 60) + giay

print(f"1. Tổng thời gian là: {tong_so_giay} giây")


# 2. Đổi 10 km sang dặm (miles)
so_km = 10
km_tren_dam = 1.61
so_dam = so_km / km_tren_dam

print(f"2. Quãng đường dài: {so_dam:.2f} dặm")


# 3. Tính Pace (nhịp độ) và Speed (tốc độ trung bình)

# Phần A: Nhịp độ trung bình (thời gian chạy 1 dặm tính bằng phút và giây)
giay_tren_dam = tong_so_giay / so_dam
pace_phut = int(giay_tren_dam // 60)  # Lấy phần nguyên để tính số phút
pace_giay = int(giay_tren_dam % 60)   # Lấy phần dư để tính số giây lẻ

print(f"3a. Nhịp độ trung bình (Pace) là: {pace_phut} phút {pace_giay} giây / dặm")

# Phần B: Tốc độ trung bình (dặm/giờ - mph)
tong_so_gio = tong_so_giay / 3600
toc_do_mph = so_dam / tong_so_gio

print(f"3b. Tốc độ trung bình là: {toc_do_mph:.2f} dặm/giờ (mph)")


#Think Python chapter 5
import time

def tinh_thoi_gian():
    tong_giay_moi = time.time()
    tong_giay = int(tong_giay_moi)
    GIAY_TRONG_PHUT = 60
    GIAY_TRONG_GIO = 3600  # 60 * 60
    GIAY_TRONG_NGAY = 86400 # 3600 * 24
    # 2. TÍNH SỐ NGÀY
    so_ngay = tong_giay // GIAY_TRONG_NGAY

    # 3. TÍNH SỐ GIÂY CÒN DƯ SAU KHI TRỪ ĐI CÁC NGÀY NGUYÊN
    giay_con_lai = tong_giay % GIAY_TRONG_NGAY

    # 4. TÍNH GIỜ
    gio = giay_con_lai // GIAY_TRONG_GIO

    # 5. TÍNH PHÚT
    giay_sau_khi_tinh_gio = giay_con_lai % GIAY_TRONG_GIO
    phut = giay_sau_khi_tinh_gio // GIAY_TRONG_PHUT

    giay = giay_sau_khi_tinh_gio % GIAY_TRONG_PHUT

    # --- HIỂN THỊ KẾT QUẢ ---
    print("-- KẾT QUẢ PHÂN TÍCH THỜI GIAN --")
    print(f"Tổng số giây từ Epoch: {tong_giay}")
    print(f"Số ngày đã trôi qua  : {so_ngay} ngày")
    print(f"Giờ hiện tại (GMT)   : {gio:02d}:{phut:02d}:{giay:02d}")
    print("-----------------------------------")

# Gọi hàm để chạy thử
tinh_thoi_gian()


# Think Python chapter 2
#bài tập 2.1
import math
r = 5
# Tính diện tích hình tròn
dien_tich = math.pi * (r ** 2)
print(f"Diện tích hình tròn có bán kính {r} là: {dien_tich:.2f}")

#bài tập 2.2
# Các thông số đầu vào
gia_bia = 24.95
chiet_khau = 0.40
so_luong = 60
# 1. Tính giá mỗi cuốn sau khi giảm 40%
gia_sau_giam = gia_bia * (1 - chiet_khau)
# 2. Tính phí vận chuyển
# Cuốn đầu là $3, 59 cuốn còn lại là $0.75/cuốn
phi_ship = 3 + (so_luong - 1) * 0.75
# 3. Tổng chi phí = (Giá sách x Số lượng) + Phí vận chuyển
tong_cong = (gia_sau_giam * so_luong) + phi_ship

print("2. Tổng chi phí bán buôn cho 60 cuốn là: $", round(tong_cong, 2))

#bài tập 2.3
# Đổi tất cả thời gian chạy sang đơn vị giây để tính cho dễ
# Chạy chậm (2 dặm): 8 phút 15 giây mỗi dặm
thoi_gian_cham = 2 * (8 * 60 + 15)
# Chạy nhanh (3 dặm): 7 phút 12 giây mỗi dặm
thoi_gian_nhanh = 3 * (7 * 60 + 12)
# Tổng cộng thời gian chạy (giây)
tong_giay_chay = thoi_gian_cham + thoi_gian_nhanh
# Tính thời điểm về đến nhà
# Xuất phát: 6 giờ 52 phút
gio_di = 6
phut_di = 52
# Cộng số phút chạy vào phút đi
tong_phut = phut_di + (tong_giay_chay // 60)
giay_du = tong_giay_chay % 60
# Xử lý việc số phút vượt quá 60 để tăng số giờ
gio_ve = gio_di + (tong_phut // 60)
phut_ve = tong_phut % 60
print(f"3. Thời gian về đến nhà là: {gio_ve}:{phut_ve}:{giay_du:02d} sáng")