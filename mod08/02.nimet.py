nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Nimi jo listalla")
    else:
        nimet.add(nimi)
        print("Nimi lisätty listalle")


print(nimet)