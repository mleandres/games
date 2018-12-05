import random
from tictactoe.board import (
  display_board,
  place_marker,
  win_check,
  full_board_check
)
from tictactoe.player import (
  player_input,
  choose_first,
  player_choice
)

def replay():
  while True:
    resp = input('Do you want to play again? [Y/N]: ').upper()
    if resp == 'Y':
      return True
    elif resp == 'N':
      return False

def game_loop():
  print('\nWelcome to Tic Tac Toe!\n')

  while True:
    # Set the game up here
    b = ['#'] + [' ']*9
    instruction_board = [str(x) for x in range(10)]

    p1, p2 = player_input()
    print('Player 1 is ' + p1 + '. Player 2 is ' + p2 + '.')

    turn = choose_first()
    print('Player '+turn+' will be going first.')
    
    print("Instructions:")
    display_board(instruction_board)

    play_game = input('Ready to play? [Y/N]: ').upper()
    game_on = play_game == 'Y'
    
    while game_on:
      # Player 1 Turn
      if turn == '1':
        # show board
        display_board(b)
        
        # choose position
        pos = player_choice(b, turn)
        
        # place marker
        place_marker(b, p1, pos)
        
        # check win
        if win_check(b, p1):
          display_board(b)
          print('Player 1 has won!')
          game_on = False
        
        # check tie
        else:
          if full_board_check(b):
            display_board(b)
            print('The game is a tie...')
            game_on = False
          else:
            # no tie or win => next player turn
            turn = '2'
  
      # Player 2 Turn
      else:
        # show board
        display_board(b)
        
        # choose position
        pos = player_choice(b, turn)
        
        # place marker
        place_marker(b, p2, pos)
        
        # check win
        if win_check(b, p2):
          display_board(b)
          print('Player 2 has won!')
          game_on = False
        
        # check tie
        else:
          if full_board_check(b):
            display_board(b)
            print('The game is a tie...')
            game_on = False
          else:
            # no tie or win => next player turn
            turn = '1'

    if not replay():
      break

if __name__ == '__main__':
  game_loop()