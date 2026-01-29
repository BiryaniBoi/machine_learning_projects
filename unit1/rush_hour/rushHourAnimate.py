import matplotlib.animation as ani
import numpy as np
import time
from rush import *
from helper import *

# SET THIS to whatever you want to use to solve
solver = astarCarsBlocking

# SET THIS to the file you want to look at
filename = "jams/easy.txt"

# SET THIS to control the fps of the animation (speed)
fps = 3

### Don't change below here! ###
cars = loadPuzzle(filename)
start = makeBoard(cars)

fig = plt.figure( figsize=(8,8) )
tick = time.time()
states, numExpanded = solver(start)
tock = time.time()
print("Time to solve: {:.3f} seconds".format(tock-tick))
print("Path length:", len(states))
print("Nodes expanded:", numExpanded)
states = states + getLastTwoStates(states[-1])
im = plot(states[0])

def animateFunc(i):
    im.set_array(states[i])
    return [im]

anim = ani.FuncAnimation(
                         fig, 
                         animateFunc, 
                         frames = len(states),
                         interval = 1000 / fps, # in ms
                         repeat=False
                         )
plt.show()
