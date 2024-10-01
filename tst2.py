fruit = int(input("How many fruits do you like:"))
Fav_fruits = []

for i in range(fruit):
    ask = input("You're favorite fruits:")
    Fav_fruits.append(ask)

    print(Fav_fruits)

for fruits in Fav_fruits:
    if fruits == "Banana":
        print("break")
        break
    elif fruits == "Apple":
        print(f"HAPPY EATING")
