a = int(input("nhap vao so thu nhat : "))
b = int(input("nhap vao so thu hai : "))
ucln = 1
for i in range(1, a+1):
    if a % i == 0 and b % i == 0 :
        ucln = i
bcnn = a * b / ucln
print(f"boi chung nho nhat la ; {bcnn}")