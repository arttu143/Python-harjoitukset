asemat = {}                                                                             #Tekee sanakirjan

while True:                                                                             #Loop alkaa
    toiminto = input("Haluatko lisätä, hakea vai lopettaa? (uusi, haku, lopeta): ")     #Kysyy haluunks uuden hakea vai lopettaa

    if toiminto == "uusi":                                                              #Jos vastasin uusi
        icao = input("Syötä lentoaseman ICAO-koodi: ")                                  #Kysyy ICAO koodin
        nimi = input("Syötä lentoaseman nimi: ")                                        #Kysyy lentokentän nimen

        asemat[icao] = nimi                                                             #Lisää ICAO koodin ja sen aseman sanakirjaan

    elif toiminto == "haku":                                                            #Jos valitsin haku
        icao = input("Syötä lentoaseman ICAO-koodi: ")                                  #Kysyy ICAO koodia

        if icao in asemat:                                                              #Jos koodi löytyi sanakirjasta
            print(asemat[icao])                                                         #Tulostaa sen
        else:                                   
            print("Lentoasemaa ei löytynyt.")                                           #Muuten tulostaa ei löytynyt

    elif toiminto == "lopeta":
        break
