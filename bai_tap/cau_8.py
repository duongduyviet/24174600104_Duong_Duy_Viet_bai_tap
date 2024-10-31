diem_chuyen_can = float(input("Nhap vao diem chuyen can: "))
diem_giua_ky = float(input("Nhap vao diem giua ky: "))
diem_cuoi_ky = float(input("nhap vao diem cuoi ky: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky)/3
if diem_chuyen_can < 0 or diem_giua_ky < 0 or diem_cuoi_ky < 0:
    print("ban da nhap sai du lieu")
elif diem_trung_binh >= 9:
    print("loai A")
elif diem_trung_binh >= 7:
    print("loai B")
elif diem_trung_binh >= 5:
    print("loai C")
else:
    print("loai D")
