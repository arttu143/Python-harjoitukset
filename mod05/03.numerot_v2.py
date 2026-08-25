numerot = []

while True:
    syote = input("Anna numero: ")

    if syote == "":
        break

    numerot.append(float(syote))

if numerot:
    print("Pienin numero:", min(numerot))
    print("Suurin numero:", max(numerot))

    #Tää oli hankala, kysyin tekoälyltä apua, nyt opin miten listoja käytetään + että min() ja max() funktiot toimii.