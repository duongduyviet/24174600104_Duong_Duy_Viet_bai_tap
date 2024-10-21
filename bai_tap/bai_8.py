import math
x = float(input("Nhap vao x: "))
if x <= 0 or x == 1:
 print("gia tri x khong thoa man")
else:
 f_x = math.log(x,4) + math.log(2,x)
 print(f"gia tri f_x la: {f_x:.2f}")
print("ket thuc chuong trinh")