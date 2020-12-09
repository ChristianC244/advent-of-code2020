def findSum(vec, sum):
    vec.sort()
    from_, _to = 0, len(vec)-1

    while from_ < _to:
        if vec[from_] + vec[_to] == sum:
            return True
        elif vec[from_] + vec[_to] < sum:
            from_ += 1
        else:
            _to -= 1

    return False


def caterpillar(vec, target):
    from_, to_ = 0, 1
    aim = 0

    while to_ < len(vec):
        aim = sum(vec[from_:to_+1])
        if aim < target: to_ += 1
        elif aim > target: from_ += 1
        else : return min(vec[from_ : to_+1 ]) + max(vec[from_ : to_+1 ])



def main():
    with open("input.txt")as file:
        vect = file.read().split(sep="\n")
    vect = [int(value) for value in vect]

    value=0
    for i in range(0, len(vect)-25):
        if not findSum(vect[i:i+25],vect[i+25]) : 
            value = vect[i+25]
            print("Solution to Part One: ", value)

    print("Solution for Part Two: ", caterpillar(vect, value))
            

if __name__ == "__main__":
    main()
