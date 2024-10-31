a_1 = float(input("Nhap a_1: "))
b_1 = float(input("Nhap b_1: "))
c_1 = float(input("Nhap c_1: "))
a_2 = float(input("Nhap a_2: "))
b_2 = float(input("Nhap b_2: "))
c_2 = float(input("Nhap c_2: "))
D = a_1 * b_2 - a_2 * b_1
Dx = c_1 * b_2 - c_2 * b_1
Dy = a_1 * c_2 - a_2 * c_1
if D != 0 :
    x = Dx/D 
    y = Dy/D
    print(f"he phuong trinh co nghiem (x,y) = {x,y}")
else :
    if Dx != 0 or Dy != 0 :
        print("he phuong trinh vo nghiem")
    else :
        print("he phuong trinh co vo sso nghiem")


