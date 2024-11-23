nhap_vao_chuoi = input("nhap vao chuoi ky tu: ")
chu_hoa = 0 
chu_thuong = 0 
for chu in nhap_vao_chuoi :
    if chu.isupper() == True :
        chu_hoa = chu_hoa + 1 
    if chu.islower() == True :
        chu_thuong = chu_thuong + 1 
print(f"so chu viet hoa la: {chu_hoa}")
print(f"so chu viet thuong la: {chu_thuong}")
