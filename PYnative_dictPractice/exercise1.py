keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

newdict = {}
#i am giving up on this activity
for x in keys:
    for y in values:
        newdict[x] = y
print("This dict is wrong ")
print(newdict)

print("(Corrections) This dict is right")
newdict.clear()
newdict = dict(zip(keys, values))
print(newdict)