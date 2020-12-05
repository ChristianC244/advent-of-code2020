def findSeat(seat, row=True):
    # Returns the value of row or column depending on the @param row given
    start = 0
    end = 127 if row else 7
    check = "F" if row else "L"

    for char in seat:
        if char == check:
            end = end - (end - start +1)/2
        else:
            start = start + (end - start +1)/2
    
    return start
    
def SeatID(seat):
    row = findSeat(seat[:-3], row = True)
    col = findSeat(seat[-3:], row = False)

    return int(row*8 +col)


def main():
    with open("input.txt") as file:
        seats = file.read().split(sep = "\n")

    # Part One
    maxSeat = SeatID(seats[0])
    for seat in seats:
        current = SeatID(seat)
        maxSeat = current if current>maxSeat else maxSeat
    print("Highest Seat ID:", maxSeat)

    #Part Two
    minSeat = maxSeat
    plane = [False]*(maxSeat+1)
    for seat in seats:
        current = SeatID(seat)
        plane[current] = True
        minSeat = current if current<minSeat else minSeat
    
    for seat in range(minSeat,maxSeat):
        if not plane[seat]:
            print("Your Seat is ",seat)
    


if __name__ == "__main__":
    main()