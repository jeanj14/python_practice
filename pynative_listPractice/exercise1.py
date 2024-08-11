#Exercise 1 of List Exercises
#This is one of exercises are from the website pyNative : https://www.pynative.com
#I will be reversing a list sorted in ascending order

list1 = [100, 200, 300, 400, 500]

newlist = []

i = len(list1)-1
while i>-1:
    newlist.append(list1[i])
    i-=1

print("Reversing list without corrections, using original solution")
print(newlist)

print("Reversing list with corrections")
list1 = list1[::-1]
print(list1)