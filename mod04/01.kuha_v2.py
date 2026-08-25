#Uusi yritys

kuhan_koko = float(input("Kuinka ison kuhan nappasit? (cm) "))
if kuhan_koko <= 37:
    print("Kuha on alamittainen, (" + str(37 - kuhan_koko) + " cm liian pieni,) joten se pitää päästää takaisin veteen.")
else:
    print("Kuha on tarpeeksi iso, joten se voi jäädä saaliiksi.") 

    #se toimii nyt jotenkin? lol