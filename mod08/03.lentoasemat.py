asemat = set()


def lentoasema():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    if icao == (""):
        return()
    kentta = input("Syötä lentoaseman nimi: ")
    if kentta == (""):
        return()                                            #Aloitin alusta
    koodi = (f"{icao}, {kentta}")
    return(koodi)


asemat.add(lentoasema())

while True:
    input1 = input("Haluatko hakea vai lisätä uuden kentän?(haku, uusi): ")
    if input1 == (""):
        break
    elif input1 == ("haku"):
        lentoasema()
