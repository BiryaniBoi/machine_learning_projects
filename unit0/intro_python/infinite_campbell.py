'''
Imagine the Campbell building has been extended infinite
floors both up and down, so that the hypothetical top
floor is +infinity and bottom floor is -infinity. That's
a lot of stairs!

You're trying to find what floor your class is on, but
the directions are a bit confusing:
^^vv would result in being on floor 0
^v^v would result in being on floor 0
^^^ would result in being on floor 3
^^v^^v^ would result in being on floor 3
vv^^^^^^ would result in being on floor 4
^vv would result in being on floor -1 
vv^ would result in being on floor -1
vvv would result in being on floor -3
v^vv^vv would result in being on floor -3
'''

def get_floor(directions):
    '''
    This function should return the floor from directions. 
    directions will be a String, and wonderfully in python a
    String behaves like a list of letters (Strings one
    character long).

    So if you do
    for direction in directions:
        # some code

    then if directions is "vv^" direction will be "v", then
    "v", then "^"
    '''
    return directions.count("^")-directions.count("v")

'''
Instead of individual directions from the ground floor
to each class, you're now given your schedule as a 
list of directions. These directions are not meant to begin
from the first floor of the building - instead, you follow
then from whatever the floor of your last class is.

You're curious what floor you'll end up on by the end of the 
day.

Let's say schedule is
["^vv", "vv^^^^^^", "vv^"]
You would start on floor -1 for your first class,
then vv^^^^^^ would take you up to floor 3 for your
second class (+4), and vv^ would take you back
down one floor (-1) to end on floor 2.

You should be able to use your get_floor function!
'''
def get_final_floor(schedule):
    return sum([get_floor(x) for x in schedule])



print(get_floor("^^vv")) # should print 0
print(get_final_floor(["^vv", "vv^^^^^^", "vv^"])) # should print 2
