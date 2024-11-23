a = int(input("nhap vao so tu so : "))
b = int(input("nhap vao so mau so : "))
ucln = 1
for i in range(1, a+1):
    if a % i == 0 and b % i == 0 :
        ucln = i
print(ucln)
tu = a / ucln
mau = b / ucln
print(f"phan so toi gian la : ({tu},{mau})")