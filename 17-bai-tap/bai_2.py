def kiem_tra_so_nguyen_duong(chuoi):
    chuoi = chuoi.strip()  
    if not chuoi: 
        return False
    if chuoi[0] in '+':  
        chuoi = chuoi[1:] 
    return chuoi.isdigit() 
