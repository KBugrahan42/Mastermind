import random
from prettytable import PrettyTable

if __name__ == "__main__":
    random_number = random.randrange(1000,9999,1)
    random_number2 = random.randrange(10000,99999,1)
    dogru = 0
    deneme = 0
    kolay_mode = False
    hard_mode = False
    myTable = PrettyTable(["Name","Score"])


    while(True):
        secim = int(input("Kolay modu secmek ister misiniz? Secmek isterseniz 1'e secmek istemiyorsanız 0'a basiniz."))
        secim2 = int(input("Zor modu secmek ister misiniz? Secmek isterseniz 1'e secmek istemiyorsaniz 0'a basiniz."))

        if(secim == 1):
            kolay_mode = True
        if(secim == 0):
            kolay_mode = False

        if(secim2 == 1):
            hard_mode = True
            break
        if(secim2 == 0):
            hard_mode = False
            break
        else:
            print("Lutfen dogru bir secim yapiniz!")
            continue

    print(random_number)
    print(random_number2)
    print(kolay_mode)
    print(hard_mode)

    while(hard_mode == False):
        try:

            sayi = int(input("Lutfen 4 basamakli tahmin ettiginiz sayiyi giriniz"))

            if(sayi != random_number):

                print("Dogru sayiyiyi bulamadiniz lutfen tekrar deneyiniz!")
                x = [int(a) for a in str(sayi)]
                y = [int(a) for a in str(random_number)]

                number = set(x) & set(y)

                if(kolay_mode == False):

                    print(f"Girdiginiz sayi ile random olusturulan sayidaki benzer rakam sayisi {len(number)}")
                if(kolay_mode == True):
                    print(x[0])
                   # print(y[0])
                    if(x[0] == y[0]):
                        print("İlk basamagi dogru tahmin ettiniz")

                    if (x[1] == y[1]):
                        print("İkinci basamagi dogru tahmin ettiniz")

                    if (x[2] == y[2]):
                        print("Ucuncu basamagi dogru tahmin ettiniz")

                    if (x[3] == y[3]):
                        print("Dorduncu basamagi dogru tahmin ettiniz")

            deneme = deneme + 1

            if(random_number == sayi):
                print(f"Tebrikler dogru sayiyi {deneme} adımda buldunuz!")
                ad = input("Lutfen adinizi giriniz")
                myTable.add_row([f"{ad}", f"{deneme}"])
                secim3 = input("Oynamaya devam etmek istiyor musunuz? Y or N")
                if (secim3 == 'Y'):
                    random_number = random.randrange(1000, 9999, 1)
                    print(random_number)
                    print(myTable)
                    deneme = 0
                    continue
                else:
                    print(myTable)
                    break
                break
        except:
            print("Lutfen sayi giriniz")

    while (hard_mode == True):
        try:
            sayi = int(input("Lutfen 5 basamakli tahmin ettiginiz sayiyi giriniz"))

            if (sayi != random_number2):

                print("Dogru sayiyiyi bulamadiniz lutfen tekrar deneyiniz!")
                x = [int(a) for a in str(sayi)]
                y = [int(a) for a in str(random_number2)]

                number = set(x) & set(y)

                if (kolay_mode == False):
                    print(f"Girdiginiz sayi ile random olusturulan sayidaki benzer rakam sayisi {len(number)}")
                if (kolay_mode == True):
                    print(x[0])
                    # print(y[0])
                    if (x[0] == y[0]):
                        print("İlk basamagi dogru tahmin ettiniz")

                    if (x[1] == y[1]):
                        print("İkinci basamagi dogru tahmin ettiniz")

                    if (x[2] == y[2]):
                        print("Ucuncu basamagi dogru tahmin ettiniz")

                    if (x[3] == y[3]):
                        print("Dorduncu basamagi dogru tahmin ettiniz")
                    if(x[4] == y[4]):
                        print("Besinci basamagi dogru tahmin ettiniz")

            deneme = deneme + 1

            if (random_number2 == sayi):
                print(f"Tebrikler dogru sayiyi {deneme} adımda buldunuz!")
                ad = input("Lutfen adinizi giriniz")
                myTable.add_row([f"{ad}",f"{deneme}"])
                secim3 = input("Oynamaya devam etmek istiyor musunuz? Y or N")
                if(secim3 == 'Y'):
                    random_number2 = random.randrange(10000, 99999, 1)
                    print(random_number2)
                    print(myTable)
                    deneme = 0
                    continue
                else:
                    print(myTable)
                    break
        except:
            print("Lutfen sayi giriniz")
