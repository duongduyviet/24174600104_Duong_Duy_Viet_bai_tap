m = int(input("nhap vap so hang cua ma tran m = "))
n = int(input("nhap vao so cot cua ma tran n = "))
ma_tran = []
print("nhap cac phan tu cua ma tran: ")
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"nhap phan tu A[{i+1}][{j+1}] = ")) 
        hang.append(phan_tu) 
    ma_tran.append(hang)  
print("ma tran co m * n vua lap la:")
for a in ma_tran:
    print(a) 
i = int(input("Nhap vao hang i: "))
j = int(input("Nhap vao hang j: "))
print("ma tran sau khi dao la")
temp = ma_tran[i-1]
ma_tran[i-1] = ma_tran[j-1]
ma_tran[j-1] = temp
for b in ma_tran:
    print(b) 