#### Connect 4 ####

def display(grid): #display board
  print('\n  ', end=" ") #end=" " makes it not go next line
                        #/n go next line

  for i in range(7): #column numbers
    print('{} '.format(i+1), end=" ")
  print()

  for i in range(6): #set tokens
    print('{}|'.format(i+1), end=" ")
    for j in range(7):
      if (grid[i+1][j] == 'x'): #detect and place player x token
        print('x ', end=" ")
      elif (grid[i+1][j] == 'o'): #detect and place player o token
        print('o ', end=" ")
      else: #detect and place empty space
        print('. ', end=" ")
    print('|')

def play(choice, grid, player): #set tokens
  for i in grid: #cycle through rows
    for j in range(8): #cycle through columns
      if (j == int(choice)): #find chosen column
        if (isinstance(grid[int(7-i)][int(j-1)], int) == True): #find row in column that is an empty space
                                                                #(int(8-i) is to find row position and im lazy simplify cause the thing daofan)
                                                                #(int(j-1) is to find column position)
          if (player == True): #player x
            grid[int(7-i)][int(j-1)] = 'x'
          else: #player o
            grid[int(7-i)][int(j-1)] = 'o'
          return grid

def winCon(grid): #detect winning combinations
  # Horizontal
  for i in grid: # For each key in grid
    for j in range(4): # For each element in list
      if((grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 'x') or (grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 'o')):
        return True

  # Vertical
  for i in range(1, 4): # i in 1, 2, 3
    for j in range(7): # For each element in list
      if((grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j] == 'x') or (grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j] == 'o')):
        return True

  # Diagonal(/)
  for i in range(1, 4): # i in 1, 2, 3
    for j in range(4): # For each element in list
      if((grid[4-i][j] == grid[4-i+1][j+1] == grid[4-i+2][j+2] == grid[4-i+3][j+3] == 'x') or (grid[4-i][j] == grid[4-i+1][j+1] == grid[4-i+2][j+2] == grid[4-i+3][j+3] == 'o')):
      # Diagonal(/) can't exist in certain keys. Key 3 is maximum for /
        return True

  # Diagonal(\)
  for i in range(1, 4): # i in 1, 2, 3
    for j in range(4): # For each element in list
      if((grid[4-i][j+3] == grid[4-i+1][j+2] == grid[4-i+2][j+1] == grid[4-i+3][j] == 'x') or (grid[4-i][j+3] == grid[4-i+1][j+2] == grid[4-i+2][j+1] == grid[4-i+3][j] == 'o')):
      # Diagonal(\) can't exist in certain keys. Key 3 is maximum for \
        return True

def drawCon(grid): #detect a draw scenario
  totalChips = 0
  for i in grid: #for each key in grid
    for j in range(7): #for each element in list
      if(grid[i][j] == "x" or grid[i][j] == "o"): #increment if slot filled up
        totalChips += 1

  if(totalChips == len(grid) * 7): #if all slots filled
    return True

def scoreboard(database): #display past wins in a scoreboard
  ranking = [] #player rankings
  scores = {'Name':[], 'Score':[]} #scoreboard
  count = 0
  database = dict(sorted(database.items(), key=lambda item: item[1], reverse=True)) #rearrange player name and score by highest

  for i in database:
    scores['Name'].append(i) #add name to scoreboard
    scores['Score'].append(database[i]) #add score to scoreboard
    count += 1
    ranking.append(count) #add ranking

  print(pd.DataFrame(scores, ranking)) #display scoreboard table DONT CHANGE

from IPython.display import clear_output #import for clearning output
import pandas as pd #import for scoreboard formatting

database = {'xx':1, 'brosboy':10}

while True:
  grid = {
      1:[1, 2, 3, 4, 5, 6, 7], 2:[1, 2, 3, 4, 5, 6, 7],
          3:[1, 2, 3, 4, 5, 6, 7], 4:[1, 2, 3, 4, 5, 6, 7],
          5:[1, 2, 3, 4, 5, 6, 7], 6:[1, 2, 3, 4, 5, 6, 7]
      }
  player = True #player = True = x, player = False = o

  clear_output()
  playerx = input('Name of player x = ') #name of first player
  playero = input('Name of player o = ') #name of second player

  display(grid)

  while True:
    if(winCon(grid) == True):
      if(player == True): #check if player is o
        print('\nGame Over!! {} wins!!\n'.format(playero)) #end game
        if playero not in database: #look for player in the scoreboard
          database.update({playero:1}) #add new player score
        else:
          database[playero] += 1 #update player score

      elif(player != True): #check if player is x
        print('\nGame Over!! {} wins!!\n'.format(playerx)) #end game
        if playerx not in database:
          database.update({playerx:1}) #add new player score
        else:
          database[playerx] += 1 #update player score

      scoreboard(database)
      input('\nEnter any key to continue... ') #restart
      break

    elif(drawCon(grid) == True):
      print('Draw!! No one wins :(\n') #end game
      scoreboard(database)
      input('\nEnter any key to continue...') #restart
      break

    else:
      if (player == True): #choose column
        choice = input('\n{} x: Column '.format(playerx))
      else:
        choice = input('\n{} o: Column '.format(playero))

      if(choice.isdigit() == True and 0 < int(choice) < 8): #check if choice is a number and check if number between 1 and 7
        clear_output()
        grid = play(choice, grid, player) #new board

        display(grid)
        player = not player #change player

      elif(choice == 'restart'): #restart
        break

      elif(choice == 'score'): #display scoreboard
        scoreboard(database)

      else:
        print('Number from 1 to 7 >:(')

