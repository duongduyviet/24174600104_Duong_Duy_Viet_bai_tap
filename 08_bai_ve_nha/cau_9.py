loai_xe = float(input("nhap vao loai xe 4 hoac 7 cho : "))
quang_duong = float(input("nhap so km : "))
thoi_gian_cho = float(input("nhap so phut cho : "))
if loai_xe == 4 :
    if quang_duong <= 20 and quang_duong > 0 :
        if thoi_gian_cho <= 5 and thoi_gian_cho > 0 :
            so_tien = (quang_duong - 0.8) * 12100 + 11000
            print(f"so tien phai tra la {so_tien}")
        elif thoi_gian_cho > 5 :
            so_tien = (quang_duong - 0.8) * 12100 + 11000 + thoi_gian_cho * 800
            print(f"so tien phai tra la {so_tien}")
        else :
            print("nhap sai du lieu")
    elif quang_duong > 20 :
        if thoi_gian_cho <= 5 and thoi_gian_cho > 0 :
            so_tien = (quang_duong - 0.8) * 10000 + 11000 
            print(f"so tien phai tra la {so_tien}")
        elif thoi_gian_cho > 5 :
            so_tien = (quang_duong - 0.8) * 10000 + 11000 + thoi_gian_cho * 800
            print(f"so tien phai tra la {so_tien}")
        else :
            print("nhap sai du lieu")
    else :
        print("nhap sai du lieu")
elif loai_xe == 7 :
    if quang_duong <= 30 and quang_duong > 0 :
        if thoi_gian_cho <= 5 and thoi_gian_cho > 0 :
            so_tien = (quang_duong - 0.8) * 14100 + 13000
            print(f"so tien phai tra la {so_tien}")
        elif thoi_gian_cho > 5 :
            so_tien = (quang_duong - 0.8) * 14100 + 13000 + thoi_gian_cho * 800
            print(f"so tien phai tra la {so_tien}")
        else :
            print("nhap sai du lieu")
    elif quang_duong > 20 :
        if thoi_gian_cho <= 5 and thoi_gian_cho > 0 :
            so_tien = (quang_duong - 0.8) * 12000 + 13000 
            print(f"so tien phai tra la {so_tien}")
        elif thoi_gian_cho > 5 :
            so_tien = (quang_duong - 0.8) * 12000 + 13000 + thoi_gian_cho * 800
            print(f"so tien phai tra la {so_tien}")
        else :
            print("nhap sai du lieu")
    else :
        print("nhap sai du lieu")
else :
    print("nhap sai du lieu")

    