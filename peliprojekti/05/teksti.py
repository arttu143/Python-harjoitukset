import time
import os


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



def lue_tiedosto(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löytynyt.")
        return ""

def tallenna_peli(pelaaja):
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{pelaaja.nimi}\n")
        tiedosto.write(f"{pelaaja.sijainti.nimi}\n")

        esineiden_nimet = [esine.nimi for esine in pelaaja.esineet]
        tiedosto.write(",".join(esineiden_nimet))

    print("Peli tallennettu!")

def lataa_peli(huoneet, esineet):
    if not os.path.exists("tallennus.txt"):
        return None

    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            nimi = tiedosto.readline().strip()
            sijainti_nimi = tiedosto.readline().strip()
            esineet_rivi = tiedosto.readline().strip()

        sijainti = None

        for huone in huoneet:
            if huone.nimi == sijainti_nimi:
                sijainti = huone
                break

        if sijainti is None:
            return None

        pelaaja = Pelaaja(nimi, sijainti)


        if esineet_rivi:
            tallennetut_esineet = esineet_rivi.split(",")

            for nimi in tallennetut_esineet:
                if nimi in esineet:
                    pelaaja.esineet.append(esineet[nimi])


                    for huone in huoneet:
                        if huone.esine is not None:
                            if huone.esine.nimi == nimi:
                                huone.esine = None

        return pelaaja

    except (FileNotFoundError, ValueError):
        return None



avain = Esine("Avain", 0.1)
kirja = Esine("Kirja", 0.5)
kivi = Esine("Kivi", 2.0)

esineet = {
    "Avain": avain,
    "Kirja": kirja,
    "Kivi": kivi
}



eteinen = Huone("Eteinen", avain)
olohuone = Huone("Olohuone", kirja)
varasto = Huone("Varasto", kivi)

huoneet = [eteinen, olohuone, varasto]



print(lue_tiedosto("intro.txt"))
print()
print(lue_tiedosto("ohjeet.txt"))
print()

pelaaja = None

if os.path.exists("tallennus.txt"):
    vastaus = input("Löytyi tallennettu peli. Haluatko jatkaa sitä? (k/e): ")

    if vastaus.lower() == "k":
        pelaaja = lataa_peli(huoneet, esineet)

        if pelaaja is not None:
            print(f"\nTervetuloa takaisin, {pelaaja.nimi}!")
            print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")
        else:
            print("Tallennuksen lataaminen epäonnistui.")

if pelaaja is None:
    nimi = input("Anna pelaajan nimi: ")
    pelaaja = Pelaaja(nimi, eteinen)

    print(f"\nTervetuloa peliin, {pelaaja.nimi}!")


#peli

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
    print("4. Tallenna peli")
    print("5. Lopeta peli")

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
        tallenna_peli(pelaaja)

    elif valinta == "5":
        tallenna_peli(pelaaja)
        print("Peli tallennettu ja lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")