import time
import random

nimi = str(input("Anna nimesi: "))
age = int(input("Anna ikäsi: "))

if age <= 12:
    print("Olet liian nuori")
    exit()
else:
    print("Olet tarpeeksi vanha, tervetuloa peliin " + nimi + "!") #onpa hankalaa
#print("""
# BLUE
#SUMMER

#1. Aloita peli.  tässä oli yritys tehdä päävalikkoa mutta eihän se noin toimi lol
#2. Tietoja
#3. Lopeta peli
#""")

while True:
    valinta = input("""
    
    BLUE
    SUMMER

    1. Aloita peli
    2. Tietoja
    3. Lopeta peli

    Valitse toiminto: 
    
    """)

    if valinta == "1":
        print("Aloitetaan peli!")
        break

    elif valinta == "2":
        print("""

Nothing here...

Palaat päävalikkoon...
""")
        time.sleep(2)
    elif valinta == "3":
        print("Lopetetaan peli. Kiitos pelaamisesta!")
        exit()

    else:
        print("Virheellinen valinta!")

#Siinä on nyt päävalikko
#Se varmaan toimii?
#Siinä numeroilla pystyy valita haluaako alottaa pelin, katsoja tietoja tai lopettaa pelin, ehkä myöhemmin lisään jotain en tiedä vielä!

