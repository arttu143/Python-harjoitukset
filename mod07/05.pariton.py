import random                                   #Importtaa random

numbers = []                                    #Tekee listan "numbers"
tasaluvut = []                                  #Tekee toisen listan "tasaluvut"

def numerot():                                  #Funktio alkaa
    for i in range(10):                         #Looppi alkaa 10 kertaa
        numero = random.randint(1, 100)         #numero = randomisti valittu luku 1-100 välillä
        numbers.append(numero)                  #Lisää numeron listaan "numbers"

        if numero % 2 == 0:                     #Laskee onko numero tasaluku
            tasaluvut.append(numero)            #Jos numero on tasaluku lisää sen listaan "tasaluvut"
numerot()                                       

print("Kaikki numerot: ", numbers)              #Tulostaa "numbers" listan 

print("Parilliset luvut: ", tasaluvut)          #tulostaa listan "tasaluvut"