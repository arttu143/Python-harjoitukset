numero = int(input("Syötä numero: "))

if numero < 2:
    print("Luku ei ole alkuluku.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("Luku ei ole alkuluku.")
            break
    else:
        print("Luku on alkuluku.")
