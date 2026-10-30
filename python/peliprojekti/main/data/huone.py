class Huone:
    def __init__(self, nimi, esine=None, kuvaus=""):
        self.nimi = nimi
        self.esine = esine
        self.kuvaus = kuvaus

        # Lista (kohdehuone, valikossa näkyvä teksti) -pareja
        self.uloskaynnit = []

        # Esine, joka pitää olla mukana ennen kuin huoneesta voi lähteä
        self.vaadittu_esine = None
        self.vaatimusviesti = ""

    def lisaa_uloskaynti(self, kohde, teksti):
        self.uloskaynnit.append((kohde, teksti))