n = input("nhap vao chuoi muon kiem tra: ")
if n.find("-") == 0 and n.count(".") <= 1 and n.find(".") != 1 :
    n_sua = n[2:].replace(".","8")
    if n_sua.isnumeric() == True :
        print(f"chuoi {n} la so am")
    else :
        print(f"chuoi {n} khong la so am")
else :
    print(f"chuoi {n} khong la so am")