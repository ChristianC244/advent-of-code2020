def jdiff(vect):
    jolts = 0
    j1, j2 = 0, 0
    j3 = 1 # Device difference

    for elem in vect:
        if elem - jolts == 1:
            j1 += 1
            jolts = elem
        elif elem - jolts == 3:
            j3 += 1
            jolts = elem
        elif elem - jolts == 2:
            j2 += 1
            jolts = elem
        else:
            print("ERROR")

    return j3*j1

def comboFinder(vect):
    length = len(vect) + 1 # Taking consideration of plug that is 0jolts
    vect = [0] + vect # Adding plug to vector

    chain=[0]*length # This vector keeps track of the total appereances of the adapter i in the various combinations
    chain[0] = 1 # Starting from one: the plane plug
    

    for i in range(length):
        adpt = vect[i]
        for j in range(i+1, min(i+4,length)):
            if vect[j]-adpt <= 3:
                chain[j] += 1*chain[i]
    
    return chain[-1] # Last value contains total usages of the last adapter, so keeps track of all the combination





def main():
    with open("input.txt") as file:
        adapters = file.read().split(sep="\n")
    adapters = [int(adapter) for adapter in adapters]
    adapters.sort()

    deviceJolts = max(adapters)+3
    print("Solution to part one is: ", jdiff(adapters))
    print("Solution to part two is: ", comboFinder(adapters))






if __name__ == "__main__":
    main()