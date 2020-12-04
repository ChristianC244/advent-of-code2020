
def treeCounterOne(Map, rule):
    right, down = rule[0], rule[1] 
    max_x, max_y = len(Map[0]), len(Map)
    x, y = 0, 0
    trees = 0

    while (y+down < max_y):
        x = (x + right) % max_x
        y += down
        if Map[y][x] == "#":
            trees += 1
    
    return trees

def main():
    rules = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    with open("input.txt") as file:
        Map = file.read().split(sep="\n")
    
    sol = 1
    for rule in rules:
        res = treeCounterOne(Map,rule)
        print("Using right: {0:d} and down: {1:d} we get: {2:d}".format(rule[0], rule[1], res) )
        sol *= res
    print("Solution: {0:d}".format(sol))


if __name__ == "__main__":
    main()