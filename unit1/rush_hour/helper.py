import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
import numpy as np

from rush import *

def loadPuzzle(filename):
    """
    Load in a puzzle from a text file
    
    Parameters
    ----------
    filename: string
        Path to puzzle
    """
    fin = open(filename)
    lines = fin.readlines()
    fin.close()
    cars = []
    for k in range(2, len(lines)):
        line = lines[k]
        fields = line.rstrip().split()
        i, j, L = int(fields[0]), int(fields[1]), int(fields[3])
        cars.append((k-2, i, j, fields[2], L))
    carLocations = getCarLocations(cars)
    return carLocations

def getCarLocations(carData):
    '''
    Returns a dictionary of carNum : list of locations
    carData is a list, with each cars in the format 
        idNumber, startRow, startCol, orientation, length.
    '''
    cars = {}
    for car in carData:
        idNum, startRow, startCol, orientation, length = car
        cars[idNum] = []
        for i in range(length):
            if orientation=='h':
                newCol = startCol + i
                cars[idNum].append((startRow, newCol))
            else:
                newRow = startRow + i
                cars[idNum].append((newRow, startCol))
    return cars

def copyCars(carsDict):
    '''
    Creates a deep copy of the cars dictionary and returns it.
    '''
    newCars = {}
    for car in carsDict:
        newCars[car]=carsDict[car][:]
    return newCars

def copyBoard(board):
    '''
    Creates a deep copy of the board and returns it.
    '''
    return [[board[r][c] for c in range(6)] for r in range(6)]


def getNumCarsOnBoard(board):
    '''
    Returns the number of cars on the board
    '''
    return max([max(row) for row in board])+1

def plot(grid):
    """
    Create a new figure and plot the state of this puzzle,
    coloring the cars by different colors
    """
    c = cm.get_cmap("Paired", getNumCarsOnBoard(grid))
    colors = [[1, 1, 1, 1], [1, 0, 0, 1]]
    colors = colors + c.colors.tolist()
    cmap = ListedColormap(colors)
    grid = np.array(grid)
    im = plt.imshow(grid, interpolation='none', cmap=cmap)
    return im

def getStringBoard(board):
    """
    Get a string representing the state

    Returns
    -------
    string: A string representation of this state
    """
    s = ""
    for i in range(6):
        for j in range(6):
            s += "%5s"%board[i][j]
        s += "\n"
    return s

def getLastTwoStates(lastState):
    '''
    Only used in rushHourAnimate, to make the animation
    look a bit nicer.
    '''
    states = []
    newState = copyBoard(lastState)
    newState[2][4]=-1
    states.append(newState)
    newState = copyBoard(newState)
    newState[2][5]=-1
    states.append(newState)
    return states

def plotSuccessors(original, successors):
    '''
    Nice color plots of all of the successors of a state. A good way
    to check that your getSuccessors is working correctly.
    '''
    N = len(successors)+1
    K = int(np.ceil(np.sqrt(N)))
    plt.figure(figsize=(8, 8))
    plt.subplot(K, K, 1)
    plt.title("Original")
    plot(original)
    for i, n in enumerate(successors):
        plt.subplot(K, K, i+2)
        plot(n)
        plt.title("Successor {}".format(i))
    plt.tight_layout()

    print("# of successors: {}".format(len(successors)))
	
