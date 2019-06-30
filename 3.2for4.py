# 10 ile 20 arasındaki asal sayıları gösterin


for num in range(10,21):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print("{} eşittir{}*{}".format(num,i,int(j)))
            break
    else:
         print(num, "asal sayıdır")
