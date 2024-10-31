import math
a = float(input("nhap vao canh thu 1 : "))
b = float(input("nhap vao canh thu 2 : "))
c = float(input("nhap vao canh thu 3 : "))
if a <= 0 or b <= 0 or c <= 0 :
    print(" a,b,c khong phai ba canh cua tam giac")
else :
 if a == b != c or a == c != b or c == b != a :
     if math.sqrt(a**2 + b**2) == c or math.sqrt(c**2 + b**2) == a or math.sqrt(a**2 + c**2) == b :
        print("day la tam giac vuong can")
     else :
        print("day la tam giac can")
 elif a == b == c :
     print("day la tam giac deu") 
 elif math.sqrt(a**2 + b**2) == c or math.sqrt(c**2 + b**2) == a or math.sqrt(a**2 + c**2) == b :
     print("day la tam giac vuong")
 else :
     print("day la tam giac thuong")
print("ket thuc chuong trinh")

    