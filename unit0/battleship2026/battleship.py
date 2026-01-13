def getShipDictionary(board):
    '''
    Returns a dictionary mapping ship types to the
    coordinates they are placed in on the board.
    Make sure "~" is not added to the dictionary since 
    it's not a ship!
    '''
    ships = {}
    for r in range(len(board)):
        for c in range(len(board[0])):
            ch = board[r][c]
            if ch != "~":
                if ch not in ships:
                    ships[ch] = []
                ships[ch].append((r,c))
    return ships

def getNumShipsRemaining(ships):
    '''
    Returns the number of ships that are still afloat 
    (i.e. ships that still have >0 coordinates remaining
    in the ships dictionary)
    '''
    return len([key for key in ships if len(ships[key]) > 0])

def makeMove(row, col, ships, board, firedAt):
    '''
    Returns True if the shot hit a ship, and False otherwise.
    If a shot was fired at a place it has been fired at previously,
    should also return False

    Updates firedAt when a new location has been targeted.
    Updates ships to remove a coordinate of a ship 
    if one has been hit.
    '''
    firedAt.add((row,col))
    hit = False
    for ship in ships:
        if (row,col) in ships[ship]:
            ships[ship].remove((row,col))
            hit = True
            break
    return hit
    
def makeHiddenBoard(board, ships, firedAt):
    '''
    Returns the "visible" version of the board based on these
    rules:
    * A location that hasn't been fired on should be water ("~")
    * A location that has been fired on and is a miss (no ship)
        should be blank (" ")
    * A location that has been fired on but is not a complete
        wrecked ship should be an asterisk ("*")
    * And lastly, a location that has been fired on where the ship
        is completely sunk should be the letter corresponding to that 
        ship (either "C", "B", "D", "S", or "P")
    '''
    new_board = []
    for r in range(len(board)):
        row = []
        for c in range(len(board[0])):
            if (r,c) in firedAt:
                if board[r][c] == "~":
                    row.append(" ")
                else:
                    ship = board[r][c]
                    row.append(ship if len(ships[ship]) == 0 else "*")
            else:
                row.append("~")
        new_board.append(row)
    return new_board

def printBoard(board, ships, firedAt, hidden=True): 
    '''
    Prints a version of the board to the terminal.
    Parameter hidden is a boolean, set to true if ships that 
    have not been hit on the board yet should remain hidden,
    false otherwise
    '''
    if hidden:
        boardToUse = makeHiddenBoard(board, ships, firedAt)
    else:
        boardToUse = board

    nums = range(len(boardToUse[0]))

    # this is terrible I know
    if len(nums) > 10:
        print(" ", end="")
    print(" " + "".join(str(n)[0] for n in nums))

    if len(nums)>10:
        print(" "*12 + "".join(str(n)[1] for n in nums[10:]))

    for r in range(len(boardToUse)):
        if len(nums) < 10 or r >= 10: # eeesh
            print(r, end="")
        elif r < 10:
            print(str(r) + " ", end="")
            
        for c in range(len(boardToUse[0])):
            print(boardToUse[r][c], end="")
        print()
    
    

