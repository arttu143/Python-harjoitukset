from data.esine import Esine
from data.huone import Huone
from data.pelaaja import Pelaaja

from pathlib import Path
import random
import sys
import time

# Tallennustiedosto sijaitsee samassa kansiossa kuin main.py,
# riippumatta siitä, mistä pelin käynnistää.
TALLENNUS = Path(__file__).parent / "tallennus.txt"

# Pelin mahdolliset lopputulokset
VOITTO = "voitto"
HAVIO = "havio"
NEUTRAALI = "neutraali"
LOPETA = "lopeta"



def lue_tiedosto(tiedostonimi):
    tiedostopolku = Path(__file__).parent / tiedostonimi

    try:
        with open(tiedostopolku, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()

    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löytynyt.")
        return ""


def luo_peli():

    # Esineet

    esineet = {
        "Megafooni": Esine("Megafooni", 0.1),
        "Vihis": Esine("Vihis", 0.5),
        "Kivi": Esine("Kivi", 2.0),
    }

    # Huoneet

    huoneet = {
        "Eteinen": Huone(
            "Eteinen",
            esineet["Megafooni"],
            "Lähdössä mielenosoitukseen. Megafoni odottaa naulakon vieressä."
        ),
        "Olohuone": Huone(
            "Olohuone",
            esineet["Vihis"],
            "Kotisi olohuone. Vihiksen ottaminen on vapaaehtoista."
        ),
        "Varasto": Huone(
            "Varasto",
            esineet["Kivi"],
            "Pimeä varasto. Täällä on jotain painavaa."
        ),
        "Kaupunki": Huone(
            "Kaupunki",
            None,
            "Kadut ovat täynnä ihmisiä."
        ),
        "Mielenosoitus": Huone(
            "Mielenosoitus",
            None,
            "Elokapinan mielenosoitus on täydessä käynnissä."
        ),
    }

    # Kulkuyhteydet

    huoneet["Eteinen"].lisaa_uloskaynti(huoneet["Olohuone"], "Olohuoneeseen")

    huoneet["Olohuone"].lisaa_uloskaynti(huoneet["Varasto"], "Varastoon")
    huoneet["Olohuone"].lisaa_uloskaynti(huoneet["Eteinen"], "Eteiseen")

    huoneet["Varasto"].lisaa_uloskaynti(huoneet["Kaupunki"], "Kaupunkiin")
    huoneet["Varasto"].lisaa_uloskaynti(huoneet["Olohuone"], "Olohuoneeseen")

    huoneet["Kaupunki"].lisaa_uloskaynti(
        huoneet["Mielenosoitus"], "Mielenosoitukseen"
    )
    huoneet["Kaupunki"].lisaa_uloskaynti(
        huoneet["Varasto"], "Takaisin varastolle"
    )

    # Esineet, joita tarvitaan ennen kuin huoneesta voi lähteä

    huoneet["Eteinen"].vaadittu_esine = esineet["Megafooni"]
    huoneet["Eteinen"].vaatimusviesti = (
        "\nEt voi vielä lähteä kotoa!\nOta megafooni mukaan."
    )

    huoneet["Varasto"].vaadittu_esine = esineet["Kivi"]
    huoneet["Varasto"].vaatimusviesti = (
        "\nEt voi vielä lähteä varastosta.\nOta kivi mukaasi."
    )

    return huoneet, esineet

def tallenna_peli(pelaaja):

    with open(TALLENNUS, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{pelaaja.nimi}\n")
        tiedosto.write(f"{pelaaja.sijainti.nimi}\n")

        esineiden_nimet = [esine.nimi for esine in pelaaja.esineet]

        tiedosto.write(",".join(esineiden_nimet))

    print("Peli tallennettu!")


def lataa_peli(huoneet, esineet):

    if not TALLENNUS.exists():
        return None

    try:
        with open(TALLENNUS, "r", encoding="utf-8") as tiedosto:
            nimi = tiedosto.readline().strip()
            sijainti_nimi = tiedosto.readline().strip()
            esineet_rivi = tiedosto.readline().strip()

        # Etsitään pelaajan sijainti
        sijainti = huoneet.get(sijainti_nimi)

        if sijainti is None:
            return None

        pelaaja = Pelaaja(nimi, sijainti)

        # Palautetaan pelaajan esineet
        if esineet_rivi:
            tallennetut_esineet = esineet_rivi.split(",")

            for esineen_nimi in tallennetut_esineet:

                if esineen_nimi in esineet:
                    pelaaja.esineet.append(esineet[esineen_nimi])

                    # Poistetaan pelaajan keräämä esine oikeasta huoneesta
                    for huone in huoneet.values():

                        if huone.esine is not None:

                            if huone.esine.nimi == esineen_nimi:
                                huone.esine = None

        return pelaaja

    except (OSError, ValueError):
        return None


def ask_age():
    while True:

        try:
            age = int(input("Anna ikäsi: "))

            if age < 12:
                print("Olet liian nuori...")
                time.sleep(2)
                sys.exit()

            return age

        except ValueError:
            print("Anna ikä numeroina.")


def aloita_pelaaja(huoneet, esineet):
    pelaaja = None

    if TALLENNUS.exists():

        vastaus = input(
            "Löytyi tallennettu peli. Haluatko jatkaa sitä? (k/e): "
        )

        if vastaus.strip().lower() == "k":

            pelaaja = lataa_peli(huoneet, esineet)

            if pelaaja is not None:
                print(f"\nTervetuloa takaisin, {pelaaja.nimi}!")
                print(f"Olet paikassa: {pelaaja.sijainti.nimi}")

            else:
                print("Tallennuksen lataaminen epäonnistui.")

    if pelaaja is None:

        nimi = input("Anna pelaajan nimi: ").strip() or "Nimetön"

        ask_age()

        pelaaja = Pelaaja(nimi, huoneet["Eteinen"])

        print(f"\nTervetuloa peliin, {pelaaja.nimi}!")

    return pelaaja



def kaupunki_saapuminen(pelaaja, vihis):
    print("\nLähdit kohti kaupunkia.")
    print("\nSaavuit kaupunkiin.")
    print("Kadut ovat täynnä ihmisiä.")
    print("Kuulet mielenosoituksen ääniä.")

    # Poliisi, satunnainen tapahtuma
    if random.randint(1, 2) == 1:

        print("\nPOLIISI PYSÄYTTÄÄ SINUT!")
        print("Poliisi haastaa sinut kamppailuun.")

        if vihis in pelaaja.esineet:
            print()
            print("Onneksi söit Vihiksen ennen kohtaamista "
                  "poliisin kanssa, joten selviät tilanteesta!")
            return None

        print("\nSinulla ei ole Vihistä, sinulla ei ole "
              "energiaa taistella.")
        print("Poliisi sai sinut kiinni.")

        print("\nJouduit putkaan, ja älylaitteesi "
              "takavarikoitiin. Laitteesta löytyi "
              "Elokapinan Telegram-kanava, jonka avulla "
              "poliisi otti kiinni kaikki jäsenet.")
        return HAVIO

    print("\nPoliisit jatkavat matkaa.")
    print("Kukaan ei huomaa sinua.")
    return None


def mielenosoitus_loppu():
    print("\nOlet mielenosoituksessa!")

    while True:

        print("\nHuudatko megafoonista?")
        print("1. Huudat")
        print("2. Et huuda")

        valinta = input("Valitse: ").strip()

        if valinta == "1":
            print("\nHuusit megafoonista. Vastamielenosoittajat "
                  "raivostuivat ja kävivät Elokapinan kimppuun, "
                  "mutta poliisit ehtivät pidättää heidät ennen kuin "
                  "sinulle kävi mitään.")
            return VOITTO

        if valinta == "2":
            print("\nPäätit olla hiljaa. Vastamielenosoittajat "
                  "voittivat ja jouduit putkaan.")
            return HAVIO

        print("Virheellinen valinta.")


def nayta_loppu(tulos):
    print()
    print("==============================")

    if tulos == VOITTO:
        print("        Voitit pelin!")

    elif tulos == HAVIO:
        print("        Hävisit pelin :(")

    elif tulos == NEUTRAALI:
        print("        Neutraali loppu")

    print("==============================")



def liiku_valikko(pelaaja, huoneet, esineet):

    nykyinen = pelaaja.sijainti

    # Vanha tallennus voi olla suoraan mielenosoituksessa
    if nykyinen is huoneet["Mielenosoitus"]:
        return mielenosoitus_loppu()

    # Tarvitaanko esine ennen lähtöä?
    if nykyinen.vaadittu_esine is not None:

        if nykyinen.vaadittu_esine not in pelaaja.esineet:
            print(nykyinen.vaatimusviesti)
            return None

    print("\nVoit mennä:")

    for numero, (kohde, teksti) in enumerate(nykyinen.uloskaynnit, start=1):
        print(f"{numero}. {teksti}")

    valinta = input("Valitse: ").strip()

    if not valinta.isdigit():
        print("Virheellinen valinta.")
        return None

    indeksi = int(valinta) - 1

    if not 0 <= indeksi < len(nykyinen.uloskaynnit):
        print("Virheellinen valinta.")
        return None

    kohde = nykyinen.uloskaynnit[indeksi][0]

    # Jänistäminen: paluu kaupungista varastolle päättää pelin
    if nykyinen is huoneet["Kaupunki"] and kohde is huoneet["Varasto"]:
        print("\nJänistit etkä mennyt mielenosoitukseen, "
              "sinut potkittiin ulos Elokapinasta.")
        return NEUTRAALI

    pelaaja.liiku(kohde)

    if kohde is huoneet["Kaupunki"]:
        return kaupunki_saapuminen(pelaaja, esineet["Vihis"])

    if kohde is huoneet["Mielenosoitus"]:
        return mielenosoitus_loppu()

    return None


def nayta_valikko(pelaaja):
    print()
    print("==============================")
    print("          PÄÄVALIKKO")
    print("==============================")

    print(f"\nOlet paikassa: {pelaaja.sijainti.nimi}")

    if pelaaja.sijainti.kuvaus:
        print(pelaaja.sijainti.kuvaus)

    # Huoneen esine
    if pelaaja.sijainti.esine is not None:
        print(f"\nPaikassa on esine: {pelaaja.sijainti.esine.nimi}")

    else:
        print("\nPaikassa ei ole esinettä.")

    print("\n1. Liiku")
    print("2. Kerää esine")
    print("3. Näytä esineet")
    print("4. Tallenna peli")
    print("5. Lopeta peli")
    print("6. Ohjeet")


def pelisilmukka(pelaaja, huoneet, esineet):
    while True:

        nayta_valikko(pelaaja)

        valinta = input("\nValitse toiminto: ").strip()

        if valinta == "1":
            tulos = liiku_valikko(pelaaja, huoneet, esineet)

            if tulos is not None:
                return tulos

        elif valinta == "2":
            pelaaja.kerää_esine()

        elif valinta == "3":
            pelaaja.näytä_esineet()

        elif valinta == "4":
            tallenna_peli(pelaaja)

        elif valinta == "5":
            tallenna_peli(pelaaja)
            print("Peli tallennettu ja lopetetaan.")
            time.sleep(3)
            return LOPETA

        elif valinta == "6":
            print()
            print(lue_tiedosto("data/ohjeet.txt"))

        else:
            print("Virheellinen valinta.")


def main():

    # Intro ja ohjeet
    print()
    print(lue_tiedosto("data/intro.txt"))
    print()
    print(lue_tiedosto("data/ohjeet.txt"))
    print()

    huoneet, esineet = luo_peli()
    pelaaja = aloita_pelaaja(huoneet, esineet)

    while True:

        tulos = pelisilmukka(pelaaja, huoneet, esineet)

        if tulos == LOPETA:
            break

        nayta_loppu(tulos)

        vastaus = input("\nHaluatko pelata uudelleen? (k/e): ")

        if vastaus.strip().lower() != "k":
            print("Kiitos pelaamisesta!")
            break

        # Uusi peli samalla nimellä
        huoneet, esineet = luo_peli()
        pelaaja = Pelaaja(pelaaja.nimi, huoneet["Eteinen"])
        print(f"\nUusi peli alkaa, {pelaaja.nimi}!")


main()