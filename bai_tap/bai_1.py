PI = 3.14
r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao (h): "))
if r > 0 and h > 0:
 dien_tich_xung_quanh = 2 * PI * r * h
 print(f"Diện tích xung quanh la: {dien_tich_xung_quanh:.2f}")
 dien_tich_toan_phan = (2 * PI * r * h) + (2 * PI * r * r)
 print(f"Diện tích toan phan la: {dien_tich_toan_phan:.2f}")
 the_tich = PI * r ** 2 * h
 print(f"the tich la: {the_tich:.2f}")
else:
 print("gia tri nhap khong thoa man")
print("ket thuc chuong trinh")