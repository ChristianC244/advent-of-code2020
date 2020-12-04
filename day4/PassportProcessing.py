'''
char = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" ]

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

'''
import re
rules = {
    "byr" : [1920, 2002],
    "iyr" : [2010, 2020],
    "eyr" : [2020, 2030],
    "cm" : [150, 193],
    "in" : [59, 76],
    "hcl" : [],
    "ecl" : ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
}

def passCheckerOne(passport):    
    elements = len(passport)
    if elements == 8:
        return True
    if elements <7:
        return False
    
    for elem in passport:
        if re.match("cid",elem):
            return False
    return True

def list2dict(vec):
    dict_pass = dict()
    vec = [stat.split(sep=":") for stat in vec ]
    for elem in vec:
        dict_pass[elem[0]]=elem[1]
    
    return dict_pass

# ---- START Checks Functions -----

def byrCheck(value):
    yr = int(value)
    return yr >= rules["byr"][0] and yr <= rules["byr"][1]

def iyrCheck(value):
    yr = int(value)
    return yr >= rules["iyr"][0] and yr <= rules["iyr"][1]

def eyrCheck(value):
    yr = int(value)
    return yr >= rules["eyr"][0] and yr <= rules["eyr"][1]

def hgtCheck(value):
    
    try:
        hgt = int(value[:-2])
    except :
        return False

    um = value[-2:]
    if um == "cm":  
        return hgt >= rules["cm"][0] and hgt <= rules["cm"][1]
    elif um == "in":
        return hgt >= rules["in"][0] and hgt <= rules["in"][1]
    
    return False

def hclCheck(value):
    if value[0] != "#":
        return False

    if len(value[1:]) != 6:
        return False

    try:
        value = int(value[1:],16)
    except:
        return False
    return True


def eclCheck(value):
    for color in rules["ecl"]:
        if value == color:
            return True
    return False

def pidCheck(value):
    if len(value) != 9:
        return False

    for char in value:
        if not char.isnumeric():
            return False

    return True

# ---- END Checks Funtions ----

def passCheckerTwo(passport):
    if not passCheckerOne(passport):
        return False

    dict_pass = list2dict(passport)

    byr = byrCheck(dict_pass["byr"])
    iyr = iyrCheck(dict_pass["iyr"])
    eyr = eyrCheck(dict_pass["eyr"])
    hgt = hgtCheck(dict_pass["hgt"])
    hcl = hclCheck(dict_pass["hcl"])
    ecl = eclCheck(dict_pass["ecl"])
    pid = pidCheck(dict_pass["pid"])
    
    return (byr and iyr and eyr and hgt and hcl and ecl and pid)


def main():
    with open("input.txt") as file:
        passports = file.read().split(sep="\n\n")

    passports = [re.split("\s", passport) for passport in passports]
    
    counterOne = 0 
    counterTwo = 0
    for psprt in passports:
        if passCheckerOne(psprt):
            counterOne +=1
        if passCheckerTwo(psprt):
            counterTwo +=1
    
    print(counterOne, counterTwo)

if __name__ == "__main__":
    main()