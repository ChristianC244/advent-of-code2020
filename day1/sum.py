sum = 2020

def partOne(vec):
    from_, _to = 0, len(vec)-1

    while from_ < _to:
        if vec[from_] + vec[_to] == sum:
            print(vec[from_]*vec[_to])
            break
        elif vec[from_] + vec[_to] < sum:
            from_ += 1
        else:
            _to -= 1
    print()

def partTwo(vec):
    for a in vec:
        for b in vec[1:]:
            for c in vec[2:]:
                if a==b or b==c or a==c:
                    break
                elif a+b+c == sum:
                    print(a*b*c)
                elif a+b+c > sum:
                    break; 



def main():
   
    with open("input.txt") as file:
        vecs = file.read().split(sep='\n')
    vec = [int(elem) for elem in vecs]
    vec.sort()
    # partOne(vec)
    partTwo(vec)


if __name__ == "__main__":
    main()