n = int(input("Nhap vao so nguyen duong n: "))
for i in range(2, n):
    for y in range(2, i):
        if i % y == 0 :
            break
    else :
        print(i)