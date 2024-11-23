n = int(input("nhap vao so de kiem tra : "))
if n <= 1:
    print(f"{n} khong phai so nguyen to")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} khong phai so nguyen to")
            break
    else:
        print(f"{n} la so nguyen to")
