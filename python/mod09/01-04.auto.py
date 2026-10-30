import random                                               #importtaa random


class Auto:                                                 
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tämänhetkinen_nopeus += muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunti


autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


#
while True:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)

    for auto in autot:
        auto.kulje(1)

    kilpailu_paattyi = False

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_paattyi = True
            break

    if kilpailu_paattyi:
        break


print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
print("-" * 60)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:15} | "
        f"{auto.huippunopeus:12} | "
        f"{auto.tämänhetkinen_nopeus:6} | "
        f"{auto.kuljettu_matka:14}"
    )

#auto2 = Auto("ABC-1", auto2nopeus)
#autot.append(auto2)

#auto = Auto("ABC-2", auto1nopeus)
#autot.append(auto)

#auto.kiihdyta(30)
#auto.kiihdyta(70)
#auto.kiihdyta(50)

#auto.kulje(1.5)

#print("Nopeus:", auto.tämänhetkinen_nopeus, "km/h")

#auto.kiihdyta(-200)

#print("Nopeus hätäjarrutuksen jälkeen:", auto.tämänhetkinen_nopeus, "km/h")



