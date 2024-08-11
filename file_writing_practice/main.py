myfile = open("test.txt", "a")

while True:
    name = input("Name: ")
    surname = input("Surname: ")
    gross = input("Gross: ")
    mystring = f" \n{name} {surname} {gross}"
    myfile.write(mystring)
    cont = input("Y or N: ").strip().upper()
    if cont == "N":
        break
