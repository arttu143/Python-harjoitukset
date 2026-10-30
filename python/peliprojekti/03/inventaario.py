import random
import time



inventaario = []


def asetukset():
    while True:
        #placeholder lisää tulee sitku pitää lool
        valinta = input("Valitse vaihtoehto!: ")
        if valinta == "":
            print("Palataan päävalikkoon.")
            time.sleep(1)
            break
            

def lopetus():
    while True:
        valinta = input("Oletko varma? (Yes / No): ")
        if valinta == "":
            print("Opettele kirjottaa!")
            continue
        elif valinta == "Yes":
            exit()
        elif valinta == "no":
            print("Hyvä valinta. Palataan päävalikkoon.")
            time.sleep(2)
            break

def add_item_inventory():
    while True:
        esine = input("Mitä haluaisit lisätä?: ")
        if esine == "":
            break
        else:
            inventaario.append(esine)
            print("Esine on lisätty inventaarioosi")
            time.sleep(2)

def print_inventory():
    for i in inventaario:
        print(i)

def pelin_aloitus():
    print("moi")

while True:
    name = input("Anna nimesi: ")

    if name == "":
        print("En usko, kokeile uudestaan.")
        continue

    break

age = int(input("Syötä ikäsi: "))

if age < 12:
    print("Olet liian nuori.")
    exit()
else:
    print(f"Olet tarpeeksi vanha! Tervetuloa {name}!")

time.sleep(2)

while True:
    print("""

          BLUE SUMMER

          1. Aloita peli
          2. Inventaario
          4. Asetukset
          3. Poistu pelistä

          """)
    valinta = input("Valitse vaihtoehto (1, 2, 3): ")
    if valinta == "":
        print("Et osaa antaa komentoja :P")
        continue
    if valinta == "1":
        pelin_aloitus()
        time.sleep(1)
        break
    elif valinta == "2":
        if inventaario:
            print("Inventaariossasi on:")
            print_inventory()
            while True:
                sekoan = input("Haluatko lisätä inventaarioon jotain? (Kyllä / Ei): ")
                if sekoan == "":
                    print("Palataan päävalikkoon.")
                    break
                elif sekoan == "Kyllä":
                    add_item_inventory()
                elif sekoan == "Ei":
                    print("Palataan päävalikkoon.")
                    time.sleep(1)
                    break
                
        else:
            print("Inventaariosi on tyhjä, lisää jotain!")
            time.sleep(1)
            add_item_inventory()

    elif valinta == "3":
        asetukset()
    elif valinta == "4":
        lopetus()