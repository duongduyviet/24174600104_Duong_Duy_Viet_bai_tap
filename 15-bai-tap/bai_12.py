ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    m = []
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = m.append(ten)
    thong_tin_sinh_vien = m.append(diem)
    ds_sinh_vien.append(thong_tin_sinh_vien)
for i in ds_sinh_vien:
    print(i)