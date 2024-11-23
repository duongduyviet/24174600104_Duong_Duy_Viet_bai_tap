chuoi_nhi_phan = input("nhap vao chuoi nhi phan: ")
for ky_tu in chuoi_nhi_phan :
    if ky_tu in "1" or ky_tu in "0" :
        chuoi_thap_phan = int(chuoi_nhi_phan, 2)
print(f"{chuoi_nhi_phan} la so nhi phan, chuyen sang thap phan: {chuoi_thap_phan}")