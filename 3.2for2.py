# dizi içerisinde yer alan elemanların ismi içerisinde m harfi bulunanların yazdırılması


sehirler = ["Adana","Ankara","Ardahan","Amasya","Edirne"]


for sehir in sehirler:
    if "m" in sehir:
        print(sehir)
    else:
        print(sehir,"şehrinde \"m\" harfi geçmemektedir")