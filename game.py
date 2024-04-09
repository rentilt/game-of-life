import pygame, sys , numpy as np
pygame.init()

# screen size
H = 600
W = 800
gameDisplay = pygame.display.set_mode((W,H))


# number of squares per line
n = 20
rows = H//n
sq_size = W//n

# init board
board = [ [np.random.randint(2) for i in range(n)] for j in range(rows)]

#beginning of logic
def draw_board(board):
    gameDisplay.fill((100,100,100))
    for i in range(1,rows+1):
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
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        draw_board(board)
        check_game()
        pygame.time.wait(300)


def check_game():
    for i in range(rows):
        for j in range(n):
            if(board[i][j]==1):
                convertToDeath(i,j)
            else:
                convertToLife(i,j)

def convertToLife(i,j):
  count = 0
  low_i = i-1 if (i-1>0) else 0
  low_j = j-1 if (j-1>0) else 0


  hi_i = i+1 if (i+1<rows) else rows-1
  hi_j = j+1 if (j+1<n) else n-1

  for x in range(low_i,hi_i+1):
    for y in range(low_j,hi_j+1):
      if(x==y):
        continue

      if(board[x][y]):
        count+=1



  if(count==3):
    #print("Mudei para vida: " ,i , j)
    board[i][j]=1

def convertToDeath(i,j):
    count = 0
    low_i = i-1 if (i-1>0) else 0
    low_j = j-1 if (j-1>0) else 0


    hi_i = i+1 if (i+1<rows) else rows-1
    hi_j = j+1 if (j+1<n) else n-1
    for x in range(low_i,hi_i+1):
        for y in range(low_j,hi_j+1):
            if(x==y):
                continue

            if(board[x][y]==1):
                count+=1


    #print(count)
    if(count<2 or count>3):
    #    print("Mudei para morte: " ,i , j)
        board[i][j]=0

if __name__ == "__main__":
    play()
