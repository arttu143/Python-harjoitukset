def pizza():                                                            #tekee funktion
    halkaisija = float(input("Mikä on pizzan halkaisija? (cm): "))      #Kysyy pizzan halkaisijaa
    hinta = float(input("Paljon pizza maksaa? (€): "))                  #Kysyy pizzan hintaa

    sade = (halkaisija / 2)                                             #Laskee pizzan säteen
    pinta_ala = (3.141 * (sade ** 2))                                   #Laskee pinta-alan
    pinta_ala_m2 = (pinta_ala / 10000)                                  #laskee pinta-alan neliömetreina

    hintaperm = (hinta / pinta_ala_m2)                                  #Laskee hinnan per neliömetri

    return hintaperm                                                    #lopettaa funktion ja antaa luvun "hintaperm"

pizza1 = pizza()                                                        #aloittaa ekan pizzan funktion
pizza2 = pizza()                                                        #Aloittaa toisen pizzan funktion

if (pizza1 > pizza2):                                                   #Vertaa pizza1 ja pizza2 hintaperm
    print("Toinen pizza on halvempi kuin ensimmäinen.")
else:
    print("Ensimmäinen pizza on halvempu kuin toinen.")