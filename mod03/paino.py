luoti = float(13.3)
naula = float(425.6)
leiviska = float(8512.0)

leiviska1 = float(input("Monta leiviskää? "))
naula1 = float(input("Monta naulaa? "))
luoti1= float(input("Monta luotia? "))

print("Paino grammoissa: " + str(leiviska1 * leiviska + naula1 * naula + luoti1 * luoti))
print("Paino kilogrammoissa: " + str((leiviska1 * leiviska + naula1 * naula + luoti1 * luoti) / 1000))
