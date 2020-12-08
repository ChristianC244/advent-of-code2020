def navigate(cmds):
    visited = [False]*len(cmds)
    acc=0
    i=0
    terminated = False
    try:
        while True:
            if cmds[i][0] == "acc":
                if not visited[i]:
                    visited[i]=True
                    acc += cmds[i][1]
                else: break

            elif cmds[i][0] == "jmp":
                if not visited[i]:
                    visited[i]=True
                    i += cmds[i][1]-1
                else: break

            else:
                if not visited[i]:
                    visited[i]=True
                else: break
            i += 1
    except:
        terminated = True
        
    return acc, terminated

# --------- Part Two


def changer(cmds, start):

    for i in range(start, len(cmds)):
        if cmds[i][0] == "jmp":
            cmds[i][0] = "nop"
            start=i
            break
        elif cmds[i][0] == "nop":
            cmds[i][0] = "jmp"
            start = i
            break

    return cmds, start

def fixer(cmds):
    acc = 0
    index = 0
    while True:
        cmds, index = changer(cmds, index)
        acc, terminated = navigate(cmds)
        if terminated:
            break
        cmds, index = changer(cmds, index)
        index += 1
 
    return acc


# ------------- Main

def main() :
    with open("input.txt") as file:
        # Reading and parsing
        cmds = file.read().split(sep="\n")
    cmds = [cmd.split(sep=" ") for cmd in cmds]
    for cmd in cmds :
        cmd[1] = int(cmd[1])


    print("Solution for Part One is: ",navigate(cmds)[0])
    print("Solution for Part Two is: ",fixer(cmds))


if __name__ == "__main__":
    main()
