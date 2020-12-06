
def groupSplitter(group):
    group = group.split(sep="\n")
    return group

def yesCounterOne(group):
    group = groupSplitter(group)
    questions = [False]*26

    for person in group:
        for answer in person:
            questions[ord(answer)%26] = True

    counter = 0
    for number in questions:
        if number:
            counter += 1
    
    return counter

def yesCounterTwo(group):
    group = groupSplitter(group)
    questions=[0]*26

    for person in group:
        for answer in person:
            questions[ord(answer)%26] += 1
    
    counter = 0
    for number in questions:
        if number == len(group):
            counter += 1
    
    return counter


def main():

    with open("input.txt") as file:
        groups = file.read().split("\n\n")

    counterOne, counterTwo = 0,0
    for group in groups:
        counterOne += yesCounterOne(group)
        counterTwo += yesCounterTwo(group)
    print("There are %d answers for part One.\nFor part Two the solution is %d " %(counterOne, counterTwo))



if __name__ == "__main__":
    main()