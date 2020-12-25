import re
def ruleSetter(vect):

    prog = re.compile("(.+): (\d+)-(\d+) or (\d+)-(\d+)")
    rules = dict()

    for line in vect:
        supa = prog.match(line)
        rules[supa.group(1)] = [ (int(supa.group(2)), int(supa.group(3))), (int(supa.group(4)), int(supa.group(5))) ]

    return rules

def errorFinder(rules, tickets):
    res = 0
    index = 0
    correctTickets = []
    
    for ticket in tickets:
        remove = False
        ticket = str2int(ticket)
        for elem in ticket:
            present = False
            for rule in rules:
                present = present or rulechecker(elem, rule, rules)
            if not present:
                remove = True
                res += elem
        if not remove:
            correctTickets.append(ticket)

    return res, correctTickets

def rulechecker( num, rule, rules):
    return ((num >=rules[rule][0][0] and num<=rules[rule][0][1]) or (num>=rules[rule][1][0] and num<=rules[rule][1][1]))

def str2int(t):
    return [int(x) for x in t.split(sep=",")]

# ------------------------ PART TWO ----------------------
def truesCounter(fields):
    
    trues = [0]*len(fields)
    for c in range(len(fields)):
        for i in range(len(fields)):
            if fields[i][c]:
                trues[c]+=1
    return trues

def fieldsBuilder(rules, tickets):

    fields = [[True]*len(rules) for i in range(len(rules))]

    for ticket in tickets:
        for elem, j  in zip(ticket, range(len(ticket))):
            for rule, i in zip(rules, range(len(rules))):
                if fields[i][j]:
                    fields[i][j] = fields[i][j] & rulechecker(elem, rule, rules)
  
    return fields

def fieldsFinder(rules, tickets):
    fields = fieldsBuilder(rules, tickets)
    template = [-1]*len(rules)
    # print(truesCounter(fields))
    flag = True
    names = list(rules)

    while flag:
        for i in range(len(fields)): #field of ticket
            trues = truesCounter(fields)
            if sum(trues) == 0:
                flag = False
                break
            if trues[i] == 1:
                for rule in range(len(fields)): # rules for field of ticket
                    if fields[rule][i]:
                        # print("elem ", i," with rule ",rule)
                        template[i] = names[rule]
                        fields[rule] = [False for x in fields[i]]
                        break
   
    return template
                    
def partTwo(fields, ticket):

    ticket = str2int(ticket)
    prog = re.compile("departure")
    res =1
    for i in range(len(fields)):
        if prog.search(fields[i]):
            res *= ticket[i]

    print("Solution to part Two: ",res)           


def main():
    with open("input.txt") as file:
        tickets = file.read().split(sep="\n")
    
    partOne = errorFinder(ruleSetter(tickets[:20]), tickets[25:])
    print("Solution to part One: ",partOne[0])
    tmp = fieldsFinder(ruleSetter(tickets[:20]), partOne[1])
    partTwo(tmp, tickets[22])


def test():
    with open("test.txt") as file:
        tickets = file.read().split(sep="\n")

    partOne = errorFinder(ruleSetter(tickets[:3]), tickets[8:])
    print(partOne[0])
    fieldsFinder(ruleSetter(tickets[:3]), partOne[1])
    

if __name__ == "__main__":
    main()