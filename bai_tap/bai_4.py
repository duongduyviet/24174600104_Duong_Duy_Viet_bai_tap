t = float(input("Nhap thoi gian su dung bong den (s): "))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
if t > 0:
 cong_suat = t*hieu_dien_the*cuong_do_dong_dien/(3600*1000)
 tien_phai_tra = cong_suat * 7000
 print(f"Tien dien phai tra la: {tien_phai_tra} dong")
else:
 print("gia tri t khong thoa man")
print("ket thuc chuong trinh")