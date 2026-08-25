import random

luku = random.randint(1, 10) 
while True:
    arvaus = int(input("Arvaa luku: "))
    if arvaus == luku:
        print("Oikein!")
        break
    elif arvaus < luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
