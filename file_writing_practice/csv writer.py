csvfile = open("test.csv" , "a")

while True:
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    csvline = f"\n{name},{surname},{age}"
    csvfile.write(csvline)
    cont = input("Y or N: ").strip().upper()
    if cont == "N":
        break

