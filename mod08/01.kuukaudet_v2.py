kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu",           
             "Huhtikuu", "Toukokuu", "Kesäkuu",
             "Heinäkuu", "Elokuu", "Syyskuu",
             "Lokakuu", "Marraskuu", "Joulukuu")

kaudet = ("talvi", "talvi", "talvi"
          "kevät", "kevät", "kevät",
          "Kesä", "Kesä", "Kesä",
          "Syksy", "Syksy", "Syksy")

numero = int(input("Syötä kuukauden järjestysnumero: "))

if numero < 1 or numero > 12:
    print("Tuntematon kuukausi")
    exit()
else:
    kuukausi = kuukaudet[numero - 1]
    kausi = kaudet[numero -1]

    print(f"{numero}. Kuukausi on {kuukausi} ja se on osa {kausi}-kautta")