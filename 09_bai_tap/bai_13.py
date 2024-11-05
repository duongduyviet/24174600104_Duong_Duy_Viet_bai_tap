n = int(input("Nhap vao so nguyen duong n: "))
for i in range(2, n):
    for y in range(2, i):
        if i % y == 0 :
            break
    else :
        if n % i == 0:
            print(i, end=" * " if n // i != i else "")