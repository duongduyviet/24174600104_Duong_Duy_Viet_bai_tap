def tim_ucln(a, b):
    ucln = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0 :
            ucln = i
    return ucln
