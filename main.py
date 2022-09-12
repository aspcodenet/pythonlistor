stefansBarn = ["Fanny", "Josefine", "Oliver"]
while True:
    print("1. Lista alla barn")
    print("2. Skriv ut hur många barn")
    print("3. Lägg till barn")
    print("4. Ta bort barn")
    print("5. Söka")
    action = input("Ange val:")
    if action == "2":
        print(f"Antal barn:{len(stefansBarn)}")
    elif action == "1":
        for namn in stefansBarn:
            print(namn)
    elif action == "3":
        namn = input("Ange namn på nya barnet")
        stefansBarn.append(namn)
    elif action == "5":
        pass
    

antal = len(stefansBarn)
print(f"Stefan har {antal} barn")

for index in range(0,antal):
    print(f"Barn nummer {index+1} heter {stefansBarn[index]}")

for namn in stefansBarn:
    print(namn)

# print(len("Stefan"))

# barn1 = "Fanny"
# barn2 = "Josefine"
# barn3 = "Oliver"
# barn4 = "Cotton"

# antal = 4
# print(f"Stefan har {antal} barn")
# print(f"Barn nummer 1 heter {barn1}" )
# print(f"Barn nummer 2 heter {barn2}" )
# print(f"Barn nummer 3 heter {barn3}" )
# print(f"Barn nummer 4 heter {barn4}" )
