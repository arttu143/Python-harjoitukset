import time


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Liikuit paikkaan: {huone.nimi}")

    def kerää_esine(self):
        if self.sijainti.esine is None:
            print("Paikassa ei ole esinettä.")
        else:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"Keräsit esineen: {esine.nimi}")

    def kokonaispaino(self):
        return sum(esine.paino for esine in self.esineet)

    def näytä_esineet(self):
        if not self.esineet:
            print("Sinulla ei ole esineitä.")
        else:
            print("Hallussasi olevat esineet:")
            for esine in self.esineet:
                print(f"- {esine.nimi}, paino {esine.paino} kg")
            print(f"Yhteensä: {self.kokonaispaino():.1f} kg")
            time.sleep(1)