# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


# Function to print a given list in a grid system
def display_board(board):
  print( f"{board[9]} | {board[8]} | {board[7]}")
  print("----------")
  print( f"{board[6]} | {board[5]} | {board[4]}")
  print("----------")
  print( f"{board[1]} | {board[2]} | {board[3]}")

test_board = ['#','X','X','X','O','X','O','X','O','X']
# print(test_board)
# Testing:
display_board(test_board)

def player_input():
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input("Player 1, choose X or O: ")
  
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

# This Function can take in a player input and assign their marker as 'X' or 'O
def place_marker(board, marker, position):
    # this is changing the original array
    board[position] = marker

# Testing:
# place_marker(test_board,'$',8)
# display_board(test_board)

# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won. *
def win_check(board, mark):
  board_marks = board[1:]
  n = 3
  print(board_marks)
  arrays_collection = [board_marks[i:i+n] for i in range (0, len(board_marks), n)]
  print(arrays_collection)

  # check for horizantal wins:
  for horiz_line in arrays_collection:
    if len(set(horiz_line)) == 1:
      print(f"{horiz_line[0]} wins")


  # for index,value in enumerate(test_board):
  #   if index == 0:
  #     pass
  #   else:
  #     horiz_triples.append(mark)
  #     print(horiz_triples)
  #     if len(set(horiz_triples)) == 1:
  #       return "WIN"


# Testing:
print(win_check(test_board,'X'))


# # might need this later
# def player_input():
#   choice = "wrong"
#   range_list = list(range(1,9))
#   # converting in a list of str to check user input
#   str_list = [str(item) for item in range_list]

#   while choice not in str_list:
#     choice = input("What cell do you choose? ")
#     if not choice.isdigit():
#       print("Please insert a value between 1 and 9")
#   return choice