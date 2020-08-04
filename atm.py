password = 1234
bakiye = 1050
print(""" 
          A) Para Çekme
          B) Para Yatırma
          C) Çıkış """)


islem = str(input("İşleminiz nedir? : "))
islem = islem.upper()
if type(islem) == str and islem == "A": 
    sayac = 0
    while sayac < 3:
        try:
            kul_sifre = int(input("Şifrenizi Giriniz: "))
            if type(kul_sifre) == int and kul_sifre == password:
                print("Hoşgeldiniz. Şu anki bakiyeniz : ", bakiye)
                try:
                    ne_kadar = int(input("Ne kadar para yatırmak istiyorsunuz? : "))
                    bakiye = bakiye + ne_kadar
                    print("Para yatırma iştemi tamamlandı . Şu anki güncel bakiyeniz :", bakiye)
                    break
                except ValueError: 
                    print("Para miktarı metinsel karakter içermemelidir.")
            else:
                sayac += 1
                if sayac == 3:
                    print("3 kez hatalı şifre girdiniz.")
        except ValueError: 
            print("Şifre metinsel karater içermemelidir.")
            break
elif type(islem) == str and islem == "B":
    sayac2 = 0
    while sayac2 < 3:
        try:
            kul_sifre = int(input("Şifrenizi Giriniz: "))
            if type(kul_sifre) == int and kul_sifre == password:
                print("Hoşgeldiniz. Şu anki bakiyeniz : ", bakiye)
                ne_kadar_cekilecek = int(input("Ne kadar para çekmek istiyorsunuz : "))
                if bakiye < ne_kadar_cekilecek:
                    print("Yeterli bakiyeniz bulunmamaktadır. ")
                    break
                else:
                    bakiye = bakiye - ne_kadar_cekilecek
                    print("Şu anki güncel bakiyeniz : ", bakiye)
                    break
        except ValueError:
            print("Değerler metinsel karakter içermemelidir.")
elif type(islem) == str and islem == "C":
    print("Çıkış yapıldı")
    pass