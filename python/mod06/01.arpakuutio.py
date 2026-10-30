import random

nopat = int(input("Montako noppaa heitetään?: "))

summa = 0

for i in range(nopat):
    tulos = random.randint(1, 6)
    summa += tulos

print("Noppien summa on: " + str(summa))