import re

def ezConverter(comp, line):
    if line[:4] == "mask":
        return line[-36:]

    res = comp.match(line)
    mem = "{0:036b}".format(int(res.group(1)))
    num = "{0:036b}".format(int(res.group(2)))

    return mem, num


def partOne(vect):

    hashTable = dict()
    memory = []
    mask=""
    counter = 0
    for line in vect:
        if len(line) == 36:
            mask = line
        else:
            mem = line[0]
            num = line[1]
            num = maskNumber(num, mask)
            if mem in hashTable.keys():
                mem = hashTable[mem]
                memory[mem] = int(num,2)
            else:
                hashTable[mem]=counter
                mem = counter
                counter += 1
                memory.append(int(num,2))
                

    return sum(memory)

def maskNumber(num, mask):
    res = ""
    for n,m in zip(num, mask):
        if m == "X":
            res +=n
        else:
            res +=m

    return res

# ------------- PART TWO --------------

def addressReader(addr, mask):
    res =""
    xCount = 0
    xPosi = []
    for a,m,i in zip(addr, mask, range(len(addr))):
        if m =="X":
            res += "X"
            xCount +=1
            xPosi.append(i)

        else:
            res += str(int(a) | int(m))
    
    
    addrs = []
    for n in range(pow(2,xCount)):
        to = 0
        add = ""
        num = "{:b}".format(n).zfill(xCount)
        j=0
        for i in xPosi:
            add += res[to:i]
            add += num[j]
            j += 1
            to = i+1
        add += res[to:]
        addrs.append(add)

    return addrs

    


def partTwo(vect):

    hashTable = dict()
    memory = []
    counter = 0
    mask=""

    for line in vect:
        addr = []
        if len(line) == 36:
            mask = line
        else:
            a = line[0]
            num = line[1]
            addr = addressReader(a, mask)
            addr = [int(a,2) for a in addr]
        for a in addr:
            if a in hashTable.keys():
                    a = hashTable[a]
                    memory[a] = int(num,2)
            else:
                hashTable[a]=counter
                counter += 1
                memory.append(int(num,2))


    return sum(memory)
    


def main():
    with open("input.txt") as file:
        initialize = file.read().split(sep="\n")
    
    prog = re.compile("mem\[(\d+)] = (\d+)")
    initialize = [ezConverter(prog,line) for line in initialize]

    print("Solution to Part One: ",partOne(initialize))
    print("Solution to Part Two: ",partTwo(initialize))



if __name__ == "__main__":
    main()