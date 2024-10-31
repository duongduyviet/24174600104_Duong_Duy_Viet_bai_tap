import math
print("toa do diem M(x,y)")
x = float(input("nhap vao x : "))
y = float(input("nhap vao y : "))
print("tao do tam I(a,b)")
a = float(input("nhap vao a : "))
b = float(input("nhap vao b : "))
r = float(input(" nhap ban kinh r : "))
do_dai_IM = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if do_dai_IM <= r :
    print("True - M(x,y) nam trong hinh tron tam I") 
else :
    print("False - M(x,y) khong nam trong hinh tron tam I")
print("ket thuc chuong trinh")