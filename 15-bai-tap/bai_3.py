while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break
A = []
B = []
for i in range(n):
    if i % 2 == 0:
        B.append(i)
    else:
        A.append(i)
A.sort(reverse=True)
B.sort(reverse=True)
print(f"danh sach A gom cac so le nho hon n la: {A}")
print(f"danh sach B gom cac so chan nho hon n la: {B}")