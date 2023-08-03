# region Tax-Free Hesaplama

price = float(input('Toplam Tutar ---> '))
cash_back = price*0.18
if price < 118:
    print('Tax-Free İçin Total Ücret 118TL den Yüksek Olmalıdır')
else:
    a = input('Tax-Free İster Misiniz ? ').lower()
    if a == 'evet':
        print(f"Cashback miktarı {cash_back}TL'dir")

# endregion


# region





# endregion