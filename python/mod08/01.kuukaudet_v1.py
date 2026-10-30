kuukaudet =("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
numero = int(input("Anna kuukauden järjestysnumero!: "))
if numero < 1 or numero > 12:
    print("Tuntematon kuukausi")
    exit()
kuukausi = kuukaudet[numero - 1]
talvi = 1, 2, 3
kevat = 4, 5, 6
kesa = 7, 8, 9
syksy = 10, 11, 12

if numero in talvi:
    print(f"{numero}. kuukausi on {kuukausi} ja se on osa talvikautta")
elif numero in kevat:
    print(f"{numero}. kuukausi on {kuukausi} ja se on osa kevätkautta")
elif numero in kesa:
    print(f"{numero}. kuukausi on {kuukausi} ja se on osa kesäkautta")
elif numero in syksy:
    print(f"{numero}. kuukausi on {kuukausi} ja se on osa syyskautta")

    #Se toimii mutta teen uudestaan...