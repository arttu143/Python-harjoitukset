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


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti = kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, litrat):
        super().__init__(rekisteritunnus, huippunopeus)
        self.litrat = litrat

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ABC-123", 165, 32.3)

auto1.kiihdyta(100)
auto2.kiihdyta(50)


auto1.kulje(3)
auto2.kulje(3)

print(f"Sähköauto: , {auto1.kuljettu_matka}, km")
print(f"Polttomoottoriauto, {auto2.kuljettu_matka}, km")