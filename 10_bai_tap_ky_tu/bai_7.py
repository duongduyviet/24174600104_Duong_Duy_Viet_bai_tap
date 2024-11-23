n = input("nhap vao chuoi muon kiem tra: ")
if n.find(".") != 0 and n.count(".") <= 1 :
    n_sua = n.replace(".","")
    if n_sua.isnumeric() == True :
        print(f"chuoi {n} la so thap phan")
    elif n.find("-") == 0 and n_sua[1:].isnumeric() == True :
        print(f"chuoi {n} la so thap phan")
    else :
        print(f"chuoi {n} khong phai la so thap phan")
else :
    print(f"chuoi {n} khong phai la so thap phan")
