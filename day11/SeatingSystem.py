'''
 L =  0 empty seat
 . = -1 floor
 # =  1 occupied seat
'''  
import copy

def seatsAround(matrix, row, col, partOne):
    # Count how many seats are occupied around the one in matrix[row][col]
      
    res =0
    seatStatus = matrix[row][col]

    if partOne:
       
        for x in range(max(row-1,0), min(row+2,len(matrix))):
            for y in range(max(col-1,0), min(col+2,len(matrix[0]))):
                if matrix[x][y]>=0:
                    res += matrix[x][y]
        
        return res-seatStatus
    else:
        directions = [-1,0],[-1,+1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1] #up,then clockwise
        for direction in directions:
            crow = row + direction[0]
            ccol = col + direction[1]
            while (crow >= 0  and crow < len(matrix)) and (ccol >= 0 and ccol < len(matrix[0])):
                if matrix[crow][ccol] >=0:
                    res += matrix[crow][ccol]
                    break
                crow += direction[0]
                ccol += direction[1]

        return res
                               


def swapper(matrix):
    # Swap ascii to int as described in the comment of the source
    subMatrix = [] #substitute
    for row in matrix:
        subRow =[]
        for elem in row:
            if elem == "L":
                subRow.append(0)
            elif elem == "#":
                subRow.append(1)
            else:
                subRow.append(-1)
        subMatrix.append(subRow)

    return subMatrix


def occupiedSeats(matrix):
    sum=0
    for row in matrix:
        for elem in row:
            if elem>=0:
                sum+=elem

    return sum

def ruleApplier(matrix,partOne):
    rows = len(matrix)
    cols = len(matrix[0])
    saves = []
    saves.append(matrix)
    saves.append(copy.deepcopy(matrix))
    flag = True

    max = 4 if partOne else 5
    
    i = 0
    while(flag):
        for x in range(rows):
            for y in range(cols):
                seat= saves[i%2][x][y]
                if seat==0 and seatsAround(saves[i%2],x,y,partOne)==0:
                    saves[(i+1) % 2][x][y] = 1
                elif seat==1 and seatsAround(saves[i%2],x,y,partOne)>=max:
                    saves[(i+1) % 2][x][y] = 0
                else:
                    saves[(i+1) % 2][x][y] = seat
        i+=1
        if saves[0]==saves[1]:
            flag = False 
    
    return occupiedSeats(saves[(i+1)%2])

def main():
    with open("input.txt") as file:
        seats = file.read().split(sep="\n")

    seats = swapper(seats)
    print(ruleApplier(seats, partOne= True))
    print(ruleApplier(seats, partOne= False))


if __name__ == "__main__":
    main()