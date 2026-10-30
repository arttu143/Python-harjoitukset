import random                                               #importtaa random et voi saada random numeroita

silmaluku = int(input("monta sivua nopassa on?: "))         #määrittää että silmaluku on käyttäjän syöttämä luku
def luku():                                                 #Funktion alku
    heitto = random.randint(1, silmaluku)                   #Määrittää että heitto on luku joka on yhden ja käyttäjän määrittämän luvun välillä
    return heitto

while True:                                                 #Looppi alkaa
    heitto = luku()                                         #Määrittää että heitto on toi funktio
    print("Heitit juuri: ",  heitto)                        #Tulostaa mitä heitit

    if heitto == silmaluku:                                 #tarkistaa onko heitto silmaluku
        print("Sait juuri maksimiluvun, onneksi olkoon!")   #Jos on nii sit tulostaa tekstin
        break                                               #lopettaa