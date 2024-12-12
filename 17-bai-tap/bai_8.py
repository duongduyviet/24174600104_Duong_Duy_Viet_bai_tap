def tim_cac_uoc_cua_mot_so_nguyen(x):
    uoc = []
    for i in range(1, x+1):
        if x % i == 0 :
            uoc.append(i)
    return uoc
print(tim_cac_uoc_cua_mot_so_nguyen(36)) 