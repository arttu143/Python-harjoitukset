import random


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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("\n" + self.nimi)
        print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
        print("-" * 60)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:15} | "
                f"{auto.huippunopeus:12} | "
                f"{auto.tämänhetkinen_nopeus:6} | "
                f"{auto.kuljettu_matka:14}"
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()


kilpailu.tulosta_tilanne()