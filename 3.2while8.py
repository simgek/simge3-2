# dışardan girilen kelimenin sesli ve sessiz harflere göre yazınız
# kaç adet sesli kaç adet sessiz harf var yaz

metin = input("lütfen bir metin giriniz :")
sesli_h = ["a","e","ı","i","o","ö","u","ü"]
i = 0
sessiz = []
sesli = []
while i < len(metin):
    if sesli_h.count(metin[i]) > 0:
        sesli.append(metin[i])
    else:
        sessiz.append(metin[i])
    i = i + 1
print("sessiz harf adedi :",len(sessiz),"\nsesli harf adedi :",len(sesli))
