import pygame, sys , numpy as np
import copy
pygame.init()

# screen size
H = 600
W = 600
gameDisplay = pygame.display.set_mode((W,H))


# number of squares per line
n = 20
rows = H//n
sq_size = W//n

def from_pos_to_cell(x, y):
    row = 0
    col = 0

    row = x // sq_size
    col = y // rows
    return (row, col)

# init board
board = [ [0 for i in range(n)] for j in range(n)]

#beginning of logic
def draw_board(board):
    gameDisplay.fill((100,100,100))
    for i in range(1,n+1):
        for j in range(1,n+1):
            #check if current loop value is even
            if board[i-1][j-1]==0:
                pygame.draw.rect(gameDisplay, (25,25,25),[sq_size*(i-1),sq_size*(j-1),sq_size,sq_size])
            else:
                pygame.draw.rect(gameDisplay, (240,240,240), [sq_size*(i-1),sq_size*(j-1),sq_size,sq_size])
            pygame.draw.rect(gameDisplay,(0,0,0),[sq_size*(i-1),sq_size*(j-1),sq_size,sq_size],1)

    # Add a nice border
    pygame.display.update()


def play():
    # make board
    print("Draw the board using the mouse (left click add cell | Right click to start game)")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    x, y = from_pos_to_cell(event.pos[0], event.pos[1])
                    board[x][y] = 1
                if event.button == 3:
                    print("Break")
                    break
            draw_board(board)
        else:
            continue 
        break

    print("Starting...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        draw_board(board)
        compute_next_board()
        pygame.time.wait(1000)


def compute_next_board():
    old_state = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):

            neighbors = count_neighbors(old_state, i,j)

            state = old_state[i][j]

            if state == 0 and neighbors == 3:
                board[i][j] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                board[i][j] = 0 

# count the number of neighbors of a cell in the board
def count_neighbors(grid, i,j):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            # wrap around
            row = (i+x) % n
            col = (j+y) % n
            count += grid[row][col]
    count -= grid[i][j]
    return count



if __name__ == "__main__":
    play()
