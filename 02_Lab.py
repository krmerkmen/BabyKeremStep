# loops

#kullancıdan alınan bir sayıya kadar olan tek sayıların küplerini ekrana yazdıran program
sayac = 0
sayi = int(input('Pozitif Bir Tam Sayı Giriniz'))
if sayi<=0 :
    print('Girdiğiniz Sayı Pozitif Değildir')
else:
    while sayac<=sayi:
        if sayac % 2 != 0:
            print((sayac**3),end=' ')
        else:
            pass
        sayac += 1

# Kullanıcıdan 2 sayı alalım birinci sayı kücük ikinci sayı büyük olsun.
# Bu iki sayı arasında kalan çift sayıları ekrana yazıran program

ks =int(input('Küçük sayıyı giriniz: '))
bs = int(input('Büyük sayıyı giriniz'))

if ks>bs:
    print('Küçük sayı büyük sayıdan büyük olamaz')
else:
    while bs>=ks:
        if ks%2==0:
            print(ks,end=',')
        ks+=1