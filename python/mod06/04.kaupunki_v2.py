kaupungit = []

while True:
    kaupunki = input("Syötä kaupunki: ")

    if kaupunki == "":
        break

    kaupungit.append(kaupunki)

for i in kaupungit:
    print(i)
