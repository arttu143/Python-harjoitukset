sade = input("Anna ympyrän säde: ")             #Pyytää käyttäjältä ympyrän säteen ja tallentaa sen "sade"
sade = float(sade)                              #Muuttaa "sade" luvun floatiksi
ympyra = 3.14 * (sade ** 2)                     #ympyra on pi kertaa sade potenssiin 2
print("Ympyrän pinta-ala on: " + str(ympyra))   #tulostaa tekstin + "ympyra"
