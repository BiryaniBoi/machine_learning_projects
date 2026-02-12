import matplotlib.pyplot as plt

from helper import *
from util import *

def makeCars(board):
    '''
    Takes in a 2D board representation and returns 
    the cars dictionary.
    '''
    cars = {}
    for r in range(len(board)):
        for c in range(len(board[0])):
            car = board[r][c]
            if car != -1:
                if car not in cars:
                    cars[car] = []
                cars[car].append((r,c))
    return cars

def makeBoard(cars):
    '''
    Takes in the cars dictionary and returns the 2D board
    representation.
    '''
    return [[find_car(cars, (r,c)) for c in range(6)] for r in range(6)]

def find_car(cars: dict, coord: tuple) -> int:
    """
    This is stupid
    """
    for car in cars:
        if coord in cars[car]:
            return car
    return -1

def isHorizontal(car_coords):
    '''
    Returns true if this is a horizontal car, and false otherwise.
    '''
    return car_coords[0][0] == car_coords[1][0]

def canMoveUp(board, car_coords):
    '''
    Returns true if this car can move up, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    vertical car the first coordinate should be the "top" of the car.
    '''
    row, col = car_coords[0]
    return (row > 0) and board[row-1][col] == -1

def canMoveDown(board, car_coords):
    '''
    Returns true if this car can move down, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    vertical car the last coordinate should be the "bottom" of the car.
    '''
    row, col = car_coords[-1]
    return (row < len(board)-1) and board[row+1][col] == -1
    

def canMoveLeft(board, car_coords):
    '''
    Returns true if this car can move right, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    horizontal car the first coordinate should be the "left" of the car.
    '''
    row, col = car_coords[0]
    return (col > 0) and board[row][col-1] == -1
    

def canMoveRight(board, car_coords):
    '''
    Returns true if this car can move up, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    horizontal car the last coordinate should be the "right" of the car.
    '''
    row, col = car_coords[-1]
    return (col < len(board)-1) and board[row][col+1] == -1
    

def getUpMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position upwards on the board.

    For example, if the coordinates of the car were
    [(1, 1), (2, 1)], this method would return
    [(0, 1), (1, 1)].
    '''
    return [(r-1,c) for r,c in car_coords]


def getDownMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position downwards on the board.

    For example, if the coordinates of the car were
    [(1, 1), (2, 1)], this method would return
    [(2, 1), (3, 1)].
    '''
    return [(r+1,c) for r,c in car_coords]

def getLeftMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position to the left on the board.

    For example, if the coordinates of the car were
    [(1, 1), (1, 2)], this method would return
    [(1, 0), (1, 1)].
    '''
    return [(r,c-1) for r,c in car_coords]

def getRightMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position to the right on the board.

    For example, if the coordinates of the car were
    [(1, 1), (1, 2)], this method would return
    [(1, 2), (1, 3)].
    '''
    return [(r,c+1) for r,c in car_coords]

def getSuccessors(board):
    '''
    How can you get the next states? 
    Make sure you use either the helper method copyCars
    or copyBoard to create a copy for each successor.
    '''
    boards = []
    cars = makeCars(board)
    for car in cars:
        coords = cars[car]
        if isHorizontal(coords):
            if canMoveLeft(board, coords):
                copyCars = makeCars(board)
                copyCars[car] = getLeftMove(coords)
                boards.append(makeBoard(copyCars))
            if canMoveRight(board, coords):
                copyCars = makeCars(board)
                copyCars[car] = getRightMove(coords)
                boards.append(makeBoard(copyCars))       
        else:
            if canMoveUp(board, coords):
                copyCars = makeCars(board)
                copyCars[car] = getUpMove(coords)
                boards.append(makeBoard(copyCars))
            if canMoveDown(board, coords):
                copyCars = makeCars(board)
                copyCars[car] = getDownMove(coords)
                boards.append(makeBoard(copyCars))
    return boards

def goalTest(board):
    '''
    The red car (car id number 0) must take up locations 
    (2,4) and (2,5) to be a "finished" search.
    '''
    return board[2][4] == 0 and board[2][5] == 0

def BFS(start):
    '''
    Implement basic BFS below, using an expanded set to speed
    up the search.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [[start]]
    expanded = set()
    while q:
        path = q.pop(0)
        board = path[-1]
        stringBoard = getStringBoard(board)
        if goalTest(board):
            return path, len(expanded)
        if stringBoard not in expanded:
            expanded.add(stringBoard)
            successors = getSuccessors(board)
            for nextBoard in successors:
                stringNext = getStringBoard(nextBoard)
                if stringNext not in expanded:
                    q.append(path + [nextBoard])

def greedySearch(start):
    '''
    Greedy search using the given heuristic

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    # below, changes heuristic being used

    ### CHANGE THIS TO CHANGE HEURISTIC ### 
    heuristic = yourHeuristic
    ###

    q = PriorityQueue()
    q.push([start], 0) 
    expanded = set()
    while not q.isEmpty():
        path = q.pop()
        board = path[-1]
        stringBoard = getStringBoard(board)
        if goalTest(board):
            return path, len(expanded)
        if stringBoard not in expanded:
            expanded.add(stringBoard)
            successors = getSuccessors(board)
            for nextBoard in successors:
                stringNext = getStringBoard(nextBoard)
                if stringNext not in expanded:
                    h = heuristic(nextBoard)
                    q.update(path + [nextBoard], h)

def distToExitHeuristic(board):
    '''
    How far is the car from the exit location?
    '''
    for c in range(len(board[0])):
        if board[2][c] == 0:
            return 4-c #find the first part of the car then subtract from 4

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    if goalTest(board):
        return 0
    #start_col = makeCars(board)[0][0][1] #get where the end of the goal car is in state S
    seen = False
    for c in range(5): #loop through all rows between where we are and where we need to be
        if board[2][c] == 0 and not seen:
            seen = True
        if seen and board[2][c] != -1 and board[2][c] != 0:
            return 2
    return 1

def yourHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write a good heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    if goalTest(board):
        return 0
    seen = False
    cars = 0
    for c in range(5):
        if board[2][c] == 0 and not seen:
            seen = True
        if seen and board[2][c] != -1 and board[2][c] != 0:
            cars += 1
    return cars + distToExitHeuristic(board)


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)

    # # uncomment for successors!
    successors = getSuccessors(board)
    plotSuccessors(board, successors)
    plt.show()
