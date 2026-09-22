class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"\nJulkaisun nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f"\nJulkaisun nimi: {self.nimi} "
              f"Julkaisun kirjoittaja: {self.kirjoittaja} "
              f"Sivumäärä: {self.sivut}")


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        print(f"\nJulkaisun nimi: {self.nimi} "
              f"Julkaisun päätoimittaja: {self.toimittaja}")


akuankka = Lehti("Aku ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

akuankka.tulosta_tiedot()
kirja.tulosta_tiedot()
