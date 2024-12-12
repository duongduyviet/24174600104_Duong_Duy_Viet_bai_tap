def kiem_tra_so_hoan_hao(x):
    uoc = 0
    for i in range(1, x) :
        if x % i == 0 :
            uoc = uoc + i
    if x == uoc :
        return True
    else :
        return False
