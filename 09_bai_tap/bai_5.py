n = int(input("nhap vao so muo0n kiem tra : "))
if n <= 1 :
    print(f"{n} khong phai so hoan hao")
else :
    uoc = 0
    for i in range(1, n) :
        if n % i == 0 :
            uoc = uoc + i
    if n == uoc :
        print(f"{n} la so hoan hao")
    else :
        print(f"{n} khong la so hoan hao")
            
            
