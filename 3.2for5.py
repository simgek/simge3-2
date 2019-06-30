# şifrenin 3 defa yanlış girilmesi dahilinde kullanıcıyı uyaran uygulama
from builtins import print

for i in range(3):
    parola = input("şifrenizi girin")
    if i == 2:
        print("şifrenizi yanlış girdiniz")
    elif not parola:
        print("şifre alanı boş bırakılamaz")
    elif len(parola) in range(3,8):
        print("paolanız:",parola ,"olarak belirlenmiştir")
        break
    else:
        print("parola yanlış")


