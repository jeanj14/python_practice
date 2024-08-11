currentNum = 2
maxNum = 100
primeNumCount = 0
primeNum = []

while (currentNum>1):
    i = currentNum
    while (i>1):
        if (currentNum % i == 0 and currentNum % 1 == 0):
            primeNum.append(currentNum)
            primeNumCount+=1
        if primeNumCount==100:
            print("The hundredth prime number is " , currentNum)
            break
    currentNum+=1

