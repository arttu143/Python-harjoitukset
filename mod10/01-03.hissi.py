class Hissi:
    def __init__(self,numero, alin, ylin):
        self.numero = numero 
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi {self.numero} on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi {self.numero} on nyt kerroksessa {self.kerros}")


class Talo:
    def __init__(self, alin, ylin, hissien_lukumaara):
        self.hissit = []

        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(i + 1, alin, ylin))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def fire(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)


talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)

talo.aja_hissiä(0, 1)

talo.fire()
