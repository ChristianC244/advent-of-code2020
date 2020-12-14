from math import ceil

def partOne(trgt, vect):
    closestDep = []
    for bus in vect:
        closestDep.append(ceil(trgt/bus)*bus)

    i = closestDep.index(min(closestDep))
    return (closestDep[i] - trgt) * vect[i]



def partTwoBF(busses, indexes): #BruteForcing
    flag = True
    n=1
    b = busses[0]
    t=0
    while flag:
        t = b*n
        for bus, i in zip(busses, indexes):
            if int((t+i)/bus) != (t+i)/bus:
                flag = True
                break
            else:
                flag = False
        n += 1
    return t

def gcdExtended(a, b):  
    if a == 0 :   
        return b,0,1 
    gcd,x1,y1 = gcdExtended(b%a, a)   
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def crt(a,b,n,m): #x = a mod(n); x = b mod(m)
    gcd, lam, mu = gcdExtended(n , m)
    x = mu*a*m + lam*b*n
    return x % (n*m), n*m


def partTwo(busses, indexes):
    
    fixedIndexes = []
    for bus, index in zip(busses, indexes):
        fixedIndexes.append((bus - index)% bus)

    t,res = crt(fixedIndexes[0], fixedIndexes[1], busses[0], busses[1])
    for i in range(2,len(busses)):
        t, res = crt(t, fixedIndexes[i], res, busses[i])

    return t

def main():

    with open("input.txt") as file:
        target = int(file.readline())
        busses = file.readline().split(sep=",")
    
    availableBusses = []
    indexes = []
    for index in range(len(busses)):
        if busses[index].isnumeric():
            indexes.append(index)
            availableBusses.append(int(busses[index]))


    print("Solution for part One is: ",partOne(target, availableBusses))
    print("Solution for part Two is: ",partTwo(availableBusses, indexes))

if __name__ == "__main__":
    main()