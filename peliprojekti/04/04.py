import time

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Liikuit huoneeseen: {huone.nimi}")

    def kerää_esine(self):
        if self.sijainti.esine is None:
            print("Huoneessa ei ole esinettä.")
        else:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"Keräsit esineen: {esine.nimi}")

    def näytä_esineet(self):
        if not self.esineet:
            print("Sinulla ei ole esineitä.")
        else:
            print("Hallussasi olevat esineet:")
            for esine in self.esineet:
                print(f"- {esine.nimi}, paino {esine.paino} kg")
            time.sleep(1)


avain = Esine("Avain", 0.1)
kirja = Esine("Kirja", 0.5)
kivi = Esine("Kivi", 2.0)

eteinen = Huone("Eteinen", avain)
olohuone = Huone("Olohuone", kirja)
varasto = Huone("Varasto", kivi)

huoneet = [eteinen, olohuone, varasto]

pelaaja = Pelaaja("Pelaaja", eteinen)


while True:
    print("\n--- PELIVALIKKO ---")
    print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")

    if pelaaja.sijainti.esine is not None:
        print(f"Huoneessa on esine: {pelaaja.sijainti.esine.nimi}")
    else:
        print("Huoneessa ei ole esinettä.")

    print("\n1. Liiku")
    print("2. Kerää esine")
    print("3. Näytä esineet")
    print("4. Lopeta peli")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        print("\nHuoneet:")
        for i, huone in enumerate(huoneet, 1):
            print(f"{i}. {huone.nimi}")

        try:
            valinta_huone = int(input("Valitse huone: "))

            if 1 <= valinta_huone <= len(huoneet):
                pelaaja.liiku(huoneet[valinta_huone - 1])
            else:
                print("Virheellinen valinta.")

        except ValueError:
            print("Anna numero.")

    elif valinta == "2":
        pelaaja.kerää_esine()

    elif valinta == "3":
        pelaaja.näytä_esineet()

    elif valinta == "4":
        print("Peli lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")