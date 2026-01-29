import matplotlib.pyplot as plt

from helper import *
from util import *

def makeCars(board):
    '''
    Takes in a 2D board representation and returns 
    the cars dictionary.
    '''
    pass

def makeBoard(cars):
    '''
    Takes in the cars dictionary and returns the 2D board
    representation.
    '''
    pass

def isHorizontal(car_coords):
    '''
    Returns true if this is a horizontal car, and false otherwise.
    '''
    pass

def canMoveUp(board, car_coords):
    '''
    Returns true if this car can move up, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    vertical car the first coordinate should be the "top" of the car.
    '''
    pass

def canMoveDown(board, car_coords):
    '''
    Returns true if this car can move down, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    vertical car the last coordinate should be the "bottom" of the car.
    '''
    pass

def canMoveLeft(board, car_coords):
    '''
    Returns true if this car can move right, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    horizontal car the first coordinate should be the "left" of the car.
    '''
    pass

def canMoveRight(board, car_coords):
    '''
    Returns true if this car can move up, and false otherwise. 
    Note that the coordinates should be in order, so if this is a
    horizontal car the last coordinate should be the "right" of the car.
    '''
    pass

def getUpMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position upwards on the board.

    For example, if the coordinates of the car were
    [(1, 1), (2, 1)], this method would return
    [(0, 1), (1, 1)].
    '''
    pass

def getDownMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position downwards on the board.

    For example, if the coordinates of the car were
    [(1, 1), (2, 1)], this method would return
    [(2, 1), (3, 1)].
    '''
    pass

def getLeftMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position to the left on the board.

    For example, if the coordinates of the car were
    [(1, 1), (1, 2)], this method would return
    [(1, 0), (1, 1)].
    '''
    pass

def getRightMove(car_coords):
    '''
    Returns a list of coordinates representing the car shifted
    one position to the right on the board.

    For example, if the coordinates of the car were
    [(1, 1), (1, 2)], this method would return
    [(1, 2), (1, 3)].
    '''
    pass

def getSuccessors(board):
    '''
    How can you get the next states? 
    Make sure you use either the helper method copyCars
    or copyBoard to create a copy for each successor.
    '''
    pass

def goalTest(board):
    '''
    The red car (car id number 0) must take up locations 
    (2,4) and (2,5) to be a "finished" search.
    '''
    pass

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
    heuristic = distToExitHeuristic
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
    pass

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    pass

def yourHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write a good heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    pass


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)

    # # uncomment for successors!
    # successors = getSuccessors(board)
    # plotSuccessors(board, successors)
    plt.show()
