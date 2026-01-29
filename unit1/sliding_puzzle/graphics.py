# graphics file for sliding puzzle game
import sys
from sliding_puzzle import *
from tkinter import *
import time

### Change these to change how the program runs!

# can be "human", "solve", solveLocation", or "solveDistance"
player = "solveLocation"
board_size = 3

OFFSET = 10
TILE_WIDTH = 70

def create_graphics_board(board, player):
	# n = len(board)**(0.5)
	n = len(board)
	window_size = n*(TILE_WIDTH+OFFSET) + OFFSET
	window = Tk()
	window.geometry(f'{window_size}x{window_size}')
	canvas = Canvas(window, width=window_size, height=window_size, bg="azure2")
	if player == "human":
		canvas.bind("<Button-1>", lambda x : click_callback(x, canvas=canvas, board=board))
	canvas.pack()

	fill_board(board, window, canvas)

	return window, canvas

def rc_to_bbox(row, col):
	x0 = OFFSET + col*(TILE_WIDTH+OFFSET)
	y0 = OFFSET + row*(TILE_WIDTH+OFFSET)
	x1 = x0+TILE_WIDTH
	y1 = y0+TILE_WIDTH
	return (x0, y0, x1, y1)

def fill_board(board, window, canvas):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]!=0:
				# x0, y0, x1, y1 = rc_to_bbox(i//3, i%3)
				x0, y0, x1, y1 = rc_to_bbox(i, j)
				canvas.create_rectangle(x0, y0, x1, y1, fill="CornflowerBlue")

				canvas.create_text(x0+TILE_WIDTH/2, y0+TILE_WIDTH/2, text=str(board[i][j]), 
									font=('Helvetica 60 bold'), justify="center")


def solve_w_path(path, window, canvas):
	
	for i in range(len(path)-1):
		row, col = path[i]
		x0, y0, x1, y1 = rc_to_bbox(row, col)

		nrow, ncol = path[i+1]
		nx0, ny0, nx1, ny1 = rc_to_bbox(nrow, ncol)
		overlapping = canvas.find_overlapping(nx0, ny0, nx1, ny1)

		canvas.moveto(overlapping[0], x0, y0)
		canvas.move(overlapping[1], x0-nx0, y0-ny0)

		window.after(500, window.update())

def board_config_to_path(configs):
	if len(configs[0]) == 2:
		return configs
	return [(i,j) for p in configs for i in range(len(p)) for j in range(len(p[0])) if p[i][j]==0]

def play_game(n, player):
	board = create_sliding_puzzle(n)
	print("Puzzle:")
	print_puzzle(board)
	window, canvas = create_graphics_board(board, player)
	if player != "human":
		window.after(200, window.update())
		print("Solving puzzle ...")
		start = time.time()
		if player == "solve":
			path = board_config_to_path(solve_puzzle(board))
		elif player == "solveLocation":
			path = board_config_to_path(solve_puzzle(board, heuristic=num_incorrect_locations))
		elif player == "solveDistance":
			path = board_config_to_path(solve_puzzle(board, heuristic=tile_manhattan_distance))
		

		print("Solved in", time.time()-start, "seconds.")
		solve_w_path(path, window, canvas)

		xpos = OFFSET + (len(board)-1)*(TILE_WIDTH+OFFSET) + TILE_WIDTH/2
		ypos = OFFSET + (len(board)-1)*(TILE_WIDTH+OFFSET) + TILE_WIDTH/2

		canvas.create_text(xpos, ypos, text='You\nwin!', font=('Helvetica 40 bold'), justify="center")

	window.mainloop()


def click_callback(event, canvas, board):
	exact_overlapping = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
	if len(exact_overlapping)!=0:
		overlapping = canvas.find_overlapping(event.x-OFFSET, event.y-OFFSET, event.x+OFFSET, event.y+OFFSET)
		if len(overlapping)==1:
			b = canvas.bbox(overlapping[0])
			overlapping = canvas.find_overlapping(b[0], b[1], b[2], b[3])
		
		d = find_direction_and_update_board(event.x, event.y, board)
		
		if d!=None:
			canvas.move(overlapping[0], d[1]*(TILE_WIDTH+OFFSET), d[0]*(TILE_WIDTH+OFFSET))
			canvas.move(overlapping[1], d[1]*(TILE_WIDTH+OFFSET), d[0]*(TILE_WIDTH+OFFSET))

		if check_victory(board):
			canvas.unbind("<Button-1>")
			xpos = OFFSET + (len(board)-1)*(TILE_WIDTH+OFFSET) + TILE_WIDTH/2
			ypos = OFFSET + (len(board)-1)*(TILE_WIDTH+OFFSET) + TILE_WIDTH/2

			canvas.create_text(xpos, ypos, text='You\nwin!', font=('Helvetica 40 bold'), justify="center")
	
def pne(p, l, m):
	return [(i, j) for i,j in [(l+1, m), (l-1, m), (l, m+1), (l, m-1)] if 0<=i<len(p) and 0<=j<len(p[0])]

def choose_random(p):
	b = find_blank(p)
	n = pne(p, b[0], b[1])
	return random.choice(n)	

def find_direction_and_update_board(x, y, board):
	'''
	should hypothetically return which way the number should move
	'''
	row = (y-OFFSET)//(TILE_WIDTH+OFFSET)
	col = (x-OFFSET)//(TILE_WIDTH+OFFSET)
	bl = find_blank(board)
	neighbors = pne(board, bl[0], bl[1])

	if (row, col) in neighbors:
		board[bl[0]][bl[1]] = board[row][col]
		board[row][col]=0
		return (bl[0]-row, bl[1]-col)

	return None

if __name__=="__main__":
	print(board_size, player)
	play_game(board_size, player)

