n = input("nhap vao chuoi ky tu: ")
chu = "".join(i for i in n if i.isalpha())
so = "".join(i for i in n if i.isnumeric())
print(f"{so}{chu}")