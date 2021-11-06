import random

# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same 
# computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then
#  place a symbol on the board

# Function to print a given list in a grid system
def display_board(board):
  # print(100 * "\n")
  print( f"{board[7]} | {board[8]} | {board[9]}")
  print("----------")
  print( f"{board[4]} | {board[5]} | {board[6]}")
  print("----------")
  print( f"{board[1]} | {board[2]} | {board[3]}")

def def_board():
    print('This are the numbers of the grid:')
    numbering_board = ['#','1','2','3','4','5','6','7','8','9']
    return display_board(numbering_board)

test_board = ['#','','X','O','X','O','O','O','X','']
# print(test_board)
# Testing:
# display_board(test_board)

def player_input():
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input("Player 1, choose X or O: ").upper()
  
  player_1 = marker
  if player_1 == "O":
    player_2 = "X"
  else:
    player_2 = "O"
  
  return (player_1, player_2)
  #tuple return

# Testing:
# player1_marker, player2_marker = player_input()
# print(player1_marker, player2_marker)

# This Function can take in a player input and assign their marker 
# as 'X' or 'O

def place_marker(board, marker, position):
    # this is changing the original array
    board[position] = marker

# Testing:
# place_marker(test_board,'$',8)
# display_board(test_board)

# Function that takes in a board and a mark (X or O) and then checks to 
# see if that mark has won.
def win_check(board, mark):
  #### need to fix this in order to make it consider
  ################################################################## work on this
  # board_marks = board[1:]
  # n = 3
  # filtered_list = [x for x in board if x != " "]
  # if len(filtered_list) >= 3:
  #   # check for diagonal wins:
  #   diag1 = []
  #   for numb in range(1,10,4):
  #     diag1.append(board[numb])
  #   print(diag1)
  #   if len(list(set(diag1))) == 1 and len(diag1) >= 3:
  #     return True
    
  #   diag2 = []
  #   for numb in range(3,10,2):
  #     diag2.append(board[numb])
  #   if len(set(diag2)) == 1 and len(diag2) >= 3:
  #     return True

  #   # check for horizontal wins:
  #   horizontal_array = [board_marks[i:i+n] for i in range (0, len(board_marks), n)]
  #   print(horizontal_array)
  #   for horiz_line in horizontal_array:
  #     filtered_horiz_list = [x for x in board if x != " "]
  #     if len(set(filtered_horiz_list)) == 1 and len(filtered_horiz_list) >= 3:
  #       return True
    
  #   # check for vertical wins:
  #   for i in range(1,4):
  #     vertical_line = []
  #     for numb in range(i,10,3):
  #       vertical_line.append(board[numb])
  #     filtered_vertic_list = [x for x in board if x != " "]
  #     if len(set(filtered_vertic_list)) == 1  and len(filtered_vertic_list) >= 3:
  #       return True
  # else:
  #   return False

  ############################################################
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
  
# Testing:
# print(win_check(test_board,'X'))

# function that uses the random module to randomly decide 
# which player goes first. You may want to lookup 
# random.randint() Return a string of which player went first.
def choose_first():
    flip = random.randint(1,2)
    if flip == 1:
      return "Player 1"
    else:
      return "Player 2"

# print(choose_first())

# This function returns a boolean indicating whether a space on the board is 
# freely available.
def space_check(board, position):
  #true if is free
  # return board[position] != "X" and board[position] != "O"
  return board[position] == ' '
 
# Testing:
# print(space_check(test_board, 2))

# function that checks if the board is full and returns a boolean value. 
# True if full, False otherwise
def full_board_check(board):
  # return board.count("X") + board.count("O") == len(board) - 1
  for i in range(1,10):
    if space_check(board, i):
        return False
  return True

# Testing:
# print(full_board_check(test_board))

# Write a function that asks for a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position

def player_choice(board):
  choice = 0
  range_list = list(range(1,10))
  # converting in a list of str to check user input
  str_list = [str(item) for item in range_list]
  
  while choice not in str_list and space_check(board,int(choice)):
    choice = input("What cell do you choose? ")
    return int(choice)
    if not choice.isdigit():
      print("Please insert a value between 1 and 9")

# Testing:
# print(player_choice(test_board))

def replay():
    return input('Play again? Enter Yes or No: ').lower().startswith('y')

# Testing:
# print(replay())

