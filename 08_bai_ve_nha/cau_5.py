ky_tu = str(input("nhap vao ki tu bat ky : "))
if ky_tu in "ueoai" :
    print("day la nguyen am")
elif ky_tu.isalpha() :
    print("day la phu am")
else :
    print("nhap sai du lieu")