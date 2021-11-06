import tictactoe

print('Welcome to Tic Tac Toe!')
print(tictactoe.def_board())

while True:
  # set up (board, who is first, choose markers x,o)
  the_board = [" "]*10
  player1_marker, player2_marker = tictactoe.player_input()



  print("Random start: ")
  print("------------------------- ")
  turn = tictactoe.choose_first()
  print(turn + " WILL GO FIRST")
  print("------------------------- ")
  play_game = input("Ready to play? Y or N? ")
  print("------------------------- ")

  if play_game == "Y":
    game_on = True
  else:
    game_on = False

  ##########################################
  # game play

  while game_on:
    if turn == "Player 1":
      # show board
      tictactoe.display_board(the_board)
      # choose a position
      position = tictactoe.player_choice(the_board)

      # place the marker on the position
      tictactoe.place_marker(the_board, player1_marker, position)

      print("------------------------- ")
      # check if they won
      if tictactoe.win_check(the_board, player1_marker):
        tictactoe.display_board(the_board)
        print("PLAYER 1 WON")
        game_on = False

      # check if it is a tie
      else:
        if tictactoe.full_board_check(the_board):
            tictactoe.display_board(the_board)
            print('The game is a draw!')
            break
        else:
          turn = "Player 2"

    else:
      # show board
      tictactoe.display_board(the_board)

      # choose a position
      position = tictactoe.player_choice(the_board)

      # place the marker on the position
      tictactoe.place_marker(the_board, player2_marker, position)

      # check if they won
      print("------------------------- ")
      if tictactoe.win_check(the_board, player2_marker):
        tictactoe.display_board(the_board)
        print("PLAYER 2 WON")
        game_on = False

      # check if it is a tie
      else:
        if tictactoe.full_board_check(the_board):
            tictactoe.display_board(the_board)
            print('The game is a draw!')
            break
        else:
          turn = "Player 1"
  print("------------------------- ")
  if not tictactoe.replay():
    break