# kullanıcıdan kullanıcı adı alalım
# en az 5 en fazla 14 karakter uzunluğunda olsun.
# kullanıcı adı sadece rakam ve kücük harf içermelidir.

from string import punctuation

name = input('Kullanıcı Adı Giriniz')
s = 0
if 5<=len(name)<=14:
    for i in name:
        if not i.isdigit() or i.islower():
            s += 1
    if s>1:
        print('Kullanıcı adı sadece kücük harf ve rakamlardan oluşmalıdır')
    else:
        print('Kullanıcı adı uygundur')
else:
    print('Kullanıcı adınız 5-14 karakter içermelidir')


# kullanıcıdan başlangıç ve adım miktarlarını alalım
# kullanıcıdan alının başlangıç miktarından başlayarak 0 a kadar adım miktarı kadar inelim
# denk gelinen sayıların karesini ekrana yazdıralım
b = int(input("Başlangıç Değeri Giriniz"))
a = int(input ("Artış Değerini Giriniz"))
for i in range(b,0,-a):
    print(i**2, end=" ")