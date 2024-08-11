# question r1.1
def is_multiple(n, m):
    result = m % n
    if result == 0:
        return True
    else:
        return False
    #function to determine if n is a multiple of m
    #m is divided by n, if result is 0, that means that the result is whole
    #meaning that the n is a multiple, else it is not a multiple
    #returns true and false based on the result


print(is_multiple(4, 20))

#question r1.4
def sumofsquares(N):

    out = 0

    for x in range(0, N):
        out+=(x**2)

    return out
#question r1.5
def sumofsquares2(M):

    out = sum([x**2 for x in range(0, M)])

    return out

print(sumofsquares(3))
print(sumofsquares2(3))

#question r1.6
def sumofoddsquares(P):
    out = 0

    for x in range(0, P):
        if x % 2 != 0:
            out+=(x**2)

    return out
#question r1.7
def sumofoddsquares2(Q):
    out = sum([x**2 for x in range(0, Q) if x % 2 != 0])
    return out

print(sumofoddsquares(5))
print(sumofoddsquares2(5))

#question r1.8
def findequivindex(s,k):
    try:
        n = len(s)
        j = 0
        if k in range(-n, 0):
            while j < n:
                if s[j] == s[k]:
                    print(f"the equivalent index to {k} is {j}")
                    break
                else:
                    j+=1
    except TypeError:
        print("No integer allowed only string")


print(findequivindex("banana", -1))

#question r1.9
for a in range(50, 90):
    if a % 10 == 0:
        print(a)
print("values 50 and 90 are sent as parameters to the range function")

#question r1.11
exponentsoftwo = [2**x for x in range(0, 9)]
print(exponentsoftwo)

