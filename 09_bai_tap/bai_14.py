n = int(input("nhap so dong tam giac : "))
for i in range(n): 
        so = 1
        for j in range(i + 1): 
            print(so, end=" ") 
            so = so * (i - j) // (j + 1) 
        print()
so = 1 
for i in range(1, n + 1): 
    for j in range(i): 
        print(so, end=" ") 
        so = so + 1  
    print() 
