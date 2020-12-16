def solverBF(init, trg):
    saves = dict()
    turn=1
    for i in init[:-1]:
        saves[i]=turn
        turn += 1
    
    current = [init[-1],-1]

    for i in range(len(init),trg):
        if current[0] in saves.keys():
            current[1] = turn - saves[current[0]]
            saves[current[0]] = turn
        else:
            saves[current[0]] = turn
            current[1] = 0
        turn+=1
        current[0]=current[1]

    return  current[0]


def main():
    with open("input.txt") as file:
        init = file.read().split(sep=",")
    init = [int(i) for i in init]    
    targetOne = 2020
    targetTwo = 30000000
    print("Solution for part One: ",solverBF(init, targetOne))
    print("Solution for part Two: ",solverBF(init, targetTwo))

if __name__ == "__main__":
    main()