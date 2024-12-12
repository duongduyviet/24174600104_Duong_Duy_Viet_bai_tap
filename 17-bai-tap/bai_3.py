def kiem_tra_so_thuc(chuoi):
    chuoi = chuoi.strip()  
    if not chuoi: 
        return False
    if chuoi[0] in ('-', '+'):  
        chuoi = chuoi[1:] 
    if chuoi.count(".") == 1:
        chuoi = chuoi.replace(".","")
    return chuoi.isdigit() 
