nhap_chuoi = input("nhap vao chuoi: ")
so_so = 0
so_chu = 0
so_ky_tu_dac_biet = 0
for chu in nhap_chuoi:
    if chu.isnumeric() == True :
        so_so = so_so + 1
    else :
        if chu.isalpha() == True :
            so_chu = so_chu + 1
        else :
            so_ky_tu_dac_biet = so_ky_tu_dac_biet + 1
print(f"So chu cai: {so_chu}")
print(f"So so: {so_so}")
print(f"So ky tu dac biet: {so_ky_tu_dac_biet}")


