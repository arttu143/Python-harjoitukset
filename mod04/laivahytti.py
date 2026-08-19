LUX = ("LUX Hytti on parvekkeellinen hytti, joka on ylä kannella.")
A = ("A Hytti on ikkunallinen hytti, joka on autokannen yläpuolella.")
B = ("B Hytti on ikkunaton hytti, joka on autokannen yläpuolella.")
C = ("C Hytti on ikkunaton hytti, joka on autokannen alapuolella.")

input = input("Anna hyttityyppi (LUX, A, B, C): ")
if input == "LUX":
    print(LUX)
elif input == "A":
    print(A)
elif input == "B":
    print(B)
elif input == "C":
    print(C)
else:
    print("Tuntematon hyttityyppi.")

    #En usko että on optimaalisin tapa tehdä tämä, mutta toimii ainakin. XD