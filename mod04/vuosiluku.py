vuosi = input("Anna vuosi: ")
vuosi = int(vuosi)
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(str(vuosi) + " on karkausvuosi.")
else:
    print(str(vuosi) + " ei ole karkausvuosi.")