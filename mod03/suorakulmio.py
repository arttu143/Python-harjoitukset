korkeus = input("Anna suorakulmion korkeus: ")
korkeus = float(korkeus)
kanta = input("Anna suorakulmion kanta: ")
kanta = float(kanta)
pinta_ala = korkeus * kanta
print("Suorakulmion pinta-ala on: " + str(pinta_ala))
print("Suorakulmion piiri on: " + str(2 * (kanta + korkeus)))