n = int(input("Nhap vao so nguyen duong n: "))
for i in range(1, n):
    uoc = 0
    for y in range(1, i):
        if i % y == 0 :
            uoc = uoc + y
    if i == uoc :
        print(i)


