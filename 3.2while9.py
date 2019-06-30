from random import randint

#print(randint(1,50)) # max 49 , min 1 değeğrini üretir

# sayısal loto rastgele 6 adet sayı üretip bunu bir dizitye ekleyiniz eğer aynı sayı dizi içerisinde geliyorsa
# tekrardan yeni bir numara üretiniz

i = 0
sayısal_loto = []
while i < 6:
    i += 1
    sayı = randint(1,49)
    if sayısal_loto.count(sayı):
        i -= 1
    else:
        sayısal_loto.append(sayı)

sayısal_loto.sort()
print(sayısal_loto)

