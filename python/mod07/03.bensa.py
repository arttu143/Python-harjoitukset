def litra(gallon):                                  #funktio alkaa
    litrat = gallon * 3.785                         #laskee annetun galloni määrän litroina
    return litrat

while True:                                         #looppi alkaa
    gallon = float(input("Syötä gallonamäärä: "))   #Pyytää galloni määrää

    if gallon < 0:                                  #Jos galloni määrä on alle 0 niin ohjelma loppuu
        break

    lasku = litra(gallon)                           #Määrittää että lasku = funktio
    print(gallon, "gallonaa on", lasku, "litraa")   #Tulostaa galloni määrän ja sen litroina.
