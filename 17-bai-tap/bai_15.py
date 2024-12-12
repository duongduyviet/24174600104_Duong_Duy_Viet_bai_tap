def kiem_tra_so_hoan_hao(x):
    uoc = 0
    for i in range(1, x) :
        if x % i == 0 :
            uoc = uoc + i
    if x == uoc :
        return True
    else :
        return False
def so_hoan_hao_nho_nhat(*args):
    # Lọc các số hoàn hảo trong dãy args
    so_hoan_hao = [num for num in args if kiem_tra_so_hoan_hao(num)]
    
    # Nếu không có số hoàn hảo, trả về None hoặc thông báo thích hợp
    if len(so_hoan_hao) == 0:
        return None
    
    # Trả về số hoàn hảo nhỏ nhất
    return min(so_hoan_hao)
print(so_hoan_hao_nho_nhat(6, 10, 28, 15))
