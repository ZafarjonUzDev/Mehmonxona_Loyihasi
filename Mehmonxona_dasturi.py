mehmonlar = {}
while True:
    print("\n<<ZafarjonUZ>> mehmonxonasiga xush kelibsiz!\nBuyruqlarni tanlang:\n\n1 -> mehmon qo'shish\n2 -> mehmonni o'chirish\n3 -> mehmonlar ro'yxati\n----------\n0 -> dasturdan chiqish\n")

    buyruq = int(input("Buyruqni yozing: "))

    if buyruq == 0:
        print("Xizmatimizdan foydalanganingiz uchun tashakkur!")
        break

    elif buyruq == 1:
        ism = input("Ism kiriting: ")

        if ism in mehmonlar:
            print(f"{ism} ro'yxatdan o'tgan!")
        else:
            while True:
                xona = input("Xona raqamini kiriting: ")
                band_xona = False
                for i in mehmonlar:
                    if mehmonlar[i]['xona'] == xona:
                        print(f"{xona}-xona bant, boshqa xona tanlang!")
                        band_xona = True
                        break
                if not band_xona:
                    break

            while True:
                tur = input("Xona turini quyidagi belgilar orqali tanlang: \ne -> Ekonom\ns -> Standart\nl -> Lyuks\nXona turi:>> ")
                if tur == 'e':
                    tur = "Ekonom"
                elif tur == 's':
                    tur = "Standart"
                elif tur == 'l':
                    tur = "Lyuks"
                else:
                    print("Qayta urinib ko'ring, xato belgi kiritildi!")
                    continue

                mehmonlar[ism] = {"xona": xona, "tur": tur}
                print(f"\n>>> {ism} mehmonimiz ro'yxatga qo'shildi!\n^^^^^^^^^^")
                break

    elif buyruq == 2:
        delet = input("Kimni ro'yxatdan o'chirmoqchisiz?: ")
        if delet in mehmonlar:
            del mehmonlar[delet]
            print(f"{delet} ro'yxatdan o'chirildi!")
        else:
            print(f"{delet} ro'yxatda mavjud emas!")

    elif buyruq == 3:
        if mehmonlar:  # agar mehmonlar bo'lsa
            print(f"\n{'Ismi:'.ljust(30)}{'Xonasi:'.ljust(30)}{'Xona turi:'.ljust(30)}")
            for k, v in mehmonlar.items():
                print(f"{k.ljust(30)}{str(v['xona']).ljust(30)}{v['tur'].ljust(30)}")
        else:
            print("Hozircha mehmonlar yo'q!")

    else:
        print("Xato buyruq kiritildi, buyruqni qayta kiriting!")