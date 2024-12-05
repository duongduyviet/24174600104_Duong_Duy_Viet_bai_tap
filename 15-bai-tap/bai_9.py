m = int(input("nhap vap so hang cua ma tran : m = "))
n = int(input("nhap vao so cot cua ma tran : n = "))
ma_tran_A = []
print("nhap cac phan tu cua ma tran A: ")
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"nhap phan tu A[{i+1}][{j+1}] = ")) 
        hang.append(phan_tu) 
    ma_tran_A.append(hang) 
ma_tran_B = []
print("nhap cac phan tu cua ma tran B: ")
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"nhap phan tu B[{i+1}][{j+1}] = ")) 
        hang.append(phan_tu) 
    ma_tran_B.append(hang)  
print("ma tran A vua lap la:")
for a in ma_tran_A:
    print(a) 
print("ma tran B vua lap la:")
for b in ma_tran_B:
    print(b) 
# print("tong 2 ma tran la")
# tong_ma_tran = []
# for i in range(m):
#     hang = []
#     for j in range(n):
#         tong_phan_tu = ma_tran_A[i][j] + ma_tran_B[i][j]
#         hang.append(tong_phan_tu) 
#     tong_ma_tran.append(hang)
# for c in tong_ma_tran:
#     print(c)
# print("hieu 2 ma tran la")
# hieu_ma_tran = []
# for i in range(m):
#     hang = []
#     for j in range(n):
#         hieu_phan_tu = ma_tran_A[i][j] - ma_tran_B[i][j]
#         hang.append(hieu_phan_tu) 
#     hieu_ma_tran.append(hang)
# for d in hieu_ma_tran:
#     print(d)
# print("tich cua ma tran A voi 1 so k la")
# k = int(input("nhap vao so k: "))
# tich_ma_tran_Ak = ma_tran_A.copy()
# for hang in range(len(tich_ma_tran_Ak)):
#     for cot in range(len(tich_ma_tran_Ak[hang])):
#         tich_ma_tran_Ak[hang][cot] = tich_ma_tran_Ak[hang][cot] * k
# for d in tich_ma_tran_Ak:
#     print(d)
print("tich 2 ma tran la")
if m != n:
    print("khong tinh duoc tich 2 ma tran")
else:
    tich_ma_tran_AB = []
    for i in range(m):
        hang = []
        tong = 0
        ton = 0
        for j in range(n):
            tong = ma_tran_A[i][j] * ma_tran_B[i][j]    
            ton = ma_tran_A[i+1][j+1] * ma_tran_B[i+1][j+1]
            
            hang.append(tong+ton)
        tich_ma_tran_AB.append(hang)
    for e in tich_ma_tran_AB:
        print(e)








