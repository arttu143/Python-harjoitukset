
nainen = "nainen".lower()
mies = "mies".lower()
muunsukupuolinen = "muunsukupuolinen".lower()

sukupuoli = input("Anna sukupuolesi, (nainen, mies, muunsukupuolinen): ").lower()
arvo = input("Anna hemoglobiiniarvosi: ")
if sukupuoli == nainen:
    if float(arvo) < 117:
        print("Hemoglobiiniarvosi on liian alhainen.")
    elif float(arvo) > 175:
        print("Hemoglobiiniarvosi on liian korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == mies:
    if float(arvo) < 134:
        print("Hemoglobiiniarvosi on liian alhainen, joten sinulla on anemia.")
    elif float(arvo) > 195:
        print("Hemoglobiiniarvosi on liian korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == muunsukupuolinen:
    if float(arvo) < 117:
        print("Hemoglobiiniarvosi on liian alhainen, joten sinulla on anemia.")
    elif float(arvo) > 195:
        print("Hemoglobiiniarvosi on liian korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

        #se toimii kai?
        #En tiiä tekeekö noi .lower() funktiot mitään, netissä sanottiin että ne tekee että ei oo välii onks kirjaimet isoi vai pienii...
        #plus ei mitään hajuu onks tää "optimaalinen tapa" tehdä tää.
        #MUT SE TOIMII (ehkä!)