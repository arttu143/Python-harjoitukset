import random

def luku():
    heitto = random.randint(1, 6)
    return heitto

while True:
    heitto = luku()
    print("Heitit juuri: ", + heitto)

    if heitto == 6:
        break