def phan_tich_nguyen_to(n):
    thua_so_nguyen_to = []
    
    while n % 2 == 0:
        thua_so_nguyen_to.append(2)
        n = n / 2  
    
    # Kiểm tra các số lẻ từ 3 trở đi
    for i in range(3, int(n), 2):
        while n % i == 0:
            thua_so_nguyen_to.append(i)
            n = n / i  # Chia n cho i
    
    # Nếu n là số nguyên tố lớn hơn 2, thêm vào danh sách
    if n > 2:
        thua_so_nguyen_to.append(n)
    
    return thua_so_nguyen_to
print(phan_tich_nguyen_to(56))
