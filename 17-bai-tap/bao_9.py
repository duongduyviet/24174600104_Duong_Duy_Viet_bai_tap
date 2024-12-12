def toi_gian_phan_so(a, b):
    ucln = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0 :
            ucln = i
    a_moi = a / ucln
    b_moi = b / ucln
    return (f"{a_moi}/{b_moi}")
print(toi_gian_phan_so(6,9))