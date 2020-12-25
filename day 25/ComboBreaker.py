modulo = 870530414842019

def loopFinder(key):
    n = 1
    c = 0
    while n!=key:
        n = (n*7) % modulo
        c += 1
    
    return c

def encriptor(subjectNumber, loop):
    value = 1
    for i in range(loop):
        value = (value * subjectNumber) % modulo
    
    return value


def main():

    with open("input.txt") as file:
        keys = file.read().split(sep = "\n")
    keys = [int(k) for k in keys]
    cardLoop = loopFinder(keys[0])
    doorLoop = loopFinder(keys[1])
    print("Solution to part One: ",encriptor(keys[0], doorLoop), encriptor(keys[1], cardLoop ))

def test():
    keys=[823448427104933, 260565059515069]
    #cardLoop = loopFinder(keys[0])
    doorLoop = loopFinder(keys[1])
    print(encriptor(keys[0], doorLoop)) #,encriptor(keys[1], cardLoop ))

if __name__ == "__main__":
    test()