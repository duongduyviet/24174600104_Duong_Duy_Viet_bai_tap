n = int(input("nhap vao so muon kiem tra "))
for i in range(n+1) :
    if i * i == n :
        print(f"{n} la so chinh phuong")
        break
else :
    print(f"{n} khong la so chinh phuong")