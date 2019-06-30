sayılar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# dizi içerisinde yer alan elamanları tek ve çift olarak ayırıp
# ayrı ayrı dizilere ekleyip ve işlem sonucunda adetleri kullanıcıya bildirmeniz

i = 0
tek = []
cift = []
while i < len(sayılar):
    if sayılar[i] % 2 == 0:
        cift.append(sayılar[i])
    else:
        tek.append(sayılar[i])
    i = i + 1
print("tek sayıların adedi :",len(tek),"\nçift sayıların adedi :",len(cift))