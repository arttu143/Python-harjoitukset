name = "python"
passwd = "rules"
wrong = 0

while True:
    user = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")

    if user == name and password == passwd:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
        wrong += 1

        if wrong == 5:
            print("Pääsy evätty")
            break