numbers = []

while True:
    user_input = input("Syötä numero: ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Suurimmat numerot ovat:")

for number in numbers[:5]:
    print(number)