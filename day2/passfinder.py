
def passReader(pwd):
    rule = pwd[0].split(sep=" ")
    letter = rule[1]
    passwd = pwd[1][1:]
    interval = rule[0].split(sep = "-")
    interval = [int(num) for num in interval]

    return letter, passwd, interval


def correctPassOne(pwd):
    letter, passwd, interval = passReader(pwd)

    counter = 0
    for char in passwd:
        if char == letter:
            counter += 1
    
    if counter >= interval[0] and counter <= interval[1]:
        return True
    return False


def correctPassTwo(pwd):
    letter, passwd, interval = passReader(pwd)

    return (passwd[interval[0]-1]==letter) ^ (passwd[interval[1]-1]==letter)
        



def main():
    with  open("pwds.txt") as file:
        pwds = file.read().split(sep="\n")

    pwds = [pwd.split(sep=":") for pwd in pwds]

    counter = 0
    for passwd in pwds:
        if correctPassTwo(passwd):
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()
    