luong = float(input("nhap so luong nhan vien (trieu) : "))
if luong < 0 :
    print("nhap sai du lieu")
elif luong < 7 :
    thue_thu_nhap = (luong * 10)/100
    luong_rong = luong - thue_thu_nhap
    print(f"thue thu nhap la : {thue_thu_nhap}")
    print(f"luong rong la : {luong_rong}")
elif luong < 15 :
    thue_thu_nhap = (luong * 20)/100
    luong_rong = luong - thue_thu_nhap
    print(f"thue thu nhap la : {thue_thu_nhap}")
    print(f"luong rong la : {luong_rong}")
else :
    thue_thu_nhap = (luong * 30)/100
    luong_rong = luong - thue_thu_nhap
    print(f"thue thu nhap la : {thue_thu_nhap}")
    print(f"luong rong la : {luong_rong}")

