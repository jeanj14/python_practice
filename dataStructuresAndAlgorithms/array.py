#list containing fruit names
#simulating a fruit market scenario with lists
fruitlist = ["banana", "apple", "pear", "grapes"]
print("Welcome to the Fruit Market\npress Q to quit loop")
while(True):
    print("which fruit do you want ?")
    usergeninput = input()
    if usergeninput.upper()=="Q":
        break
    try:
        fruitindex = fruitlist.index(usergeninput)
        print(fruitlist.pop(fruitindex))
    except ValueError:
        print("The fruit is not in the basket. Try again")

