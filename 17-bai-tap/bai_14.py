def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def trung_binh_so_nguyen_to(*args):
    so_nguyen_to = [num for num in args if kiem_tra_so_nguyen_to(num)]
    if len(so_nguyen_to) == 0:
        return 0
    trung_binh = sum(so_nguyen_to) / len(so_nguyen_to)
    return trung_binh
print(trung_binh_so_nguyen_to(2, 3, 4, 5, 6))