import random                                       #random

numbers = []                                        #tekee listan

def numerot():                                      #Funktion alku
    for i in range(5):                              #Looppaa viidesti
        numero = random.randint(1, 100)             #Valitsee numeron 1-100 välillä
        numbers.append(numero)                      #Lisää numeron listaan
    return numbers                                  #Palaa loopin alkuun

print("Numerot ovat:", numerot())                   #Printtaa random numerot
print("Yhteenlaskettu summa on:", sum(numbers))     #Laskee numeroiden summan

                                                    #En osaa sanoa oliko tämä oikea tehtävän pyyntö