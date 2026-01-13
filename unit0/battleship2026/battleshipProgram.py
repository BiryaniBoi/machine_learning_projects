from computerHelper import *
from battleship import *
import os

board = initializeGameBoard()
firedAt = set()
ships = getShipDictionary(board)
turns = 0


# your code goes here!
#NOTE: we only count the turns where players miss
print("Welcome to Battleship!")
print("shhhhh")
printBoard(board, ships, firedAt, False)
printBoard(board, ships, firedAt)
print(f"You have {getNumShipsRemaining(ships)} remaining.")
while getNumShipsRemaining(ships) > 0:
    print("Where would you like to guess?")
    row = int(input("Row: "))
    col = int(input("Column: "))
    while (row,col) in firedAt:
        print(f"You've already shot at ({row},{col}). Please pick a new location")
        row = int(input("Row: "))
        col = int(input("Column: "))
    hit = makeMove(row, col, ships, board, firedAt)
    if hit:
        print("Hit!")
        print(f"You have {getNumShipsRemaining(ships)} remaining.")
    else:
        print("Miss!")
    print(f"You've fired at {firedAt}")
    printBoard(board, ships, firedAt)
    if not hit:
        turns += 1
    
print("You've sunk all the ship! You Win!")

path = "highscore.txt"

if os.path.isfile(path):
    file = open(path)
    highscore = int(file.read())
    if turns < highscore:
        highscore = turns
        file.write(str(highscore))
    file.close()
    print(f"You took {turns} turns to sink all the ships!")
    print(f"The highscore is {turns} turns!")
else:
    print(f"You took {turns} turns to sink all the ships!")
    file = open(path, "w")
    file.write(str(turns))
    file.close()

