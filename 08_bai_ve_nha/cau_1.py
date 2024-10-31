nam = float(input(" nhap so nam : "))
if nam > 0 :
 if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0 :
  print("day la nam nhuan")
 else :
  print("day khong la nam nhuan")
else :
 print("nhap sai du lieu")
print("ket thuc chuong trinh")