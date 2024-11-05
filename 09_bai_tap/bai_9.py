n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n):
    for y in range(i):
        if y ** y == i:
            print(i)
