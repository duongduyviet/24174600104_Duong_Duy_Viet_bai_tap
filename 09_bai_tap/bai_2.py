n = int(input("Nhap vao so nguyen duong n: "))
if n <= 0 :
    print("nhap sai du lieu")
else :
    tong_S1 = 0
    for i in range(1, n + 1):
        tong_S1 = tong_S1 + i
    print(f"tong_S1 la : {tong_S1}")

    tich_S2 = 1
    for a in range(1, n):
        tich_S2 = tich_S2 * a
    print(f"tich_S2 la : {tich_S2}")

    tong_S3 = 0
    for i in range(1, n + 1):
        tong_S3 = tong_S3 + ((-1) ** (i + 1)) / i
    print(f"tong_S3 la : {tong_S3}")

    tong_S4 = 0
    for k in range(1, n + 1):
        tong_S4 = tong_S4 + k/(k+2)
    print(f"tong_S4 la : {tong_S4}")
