import random
from tictactoe.board import space_check

def player_input():
    marker = ''
    # keep asking player 1 to choose X or O
    while True:
        marker = input('Player 1, choose X or O: ').upper()
        if marker == 'X' or marker =='O':
          break
        print('Invalid choice.')
    
    # assign player 2 the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def choose_first():
    r = random.randint(1,2)
    return str(r)

def player_choice(board, player):
  choice = 0
  while True:
    try:
      choice = int(input(f'Player {player}: Enter a number to between [1-9]: '))
      if space_check(board,choice):
        break
    except ValueError:
      print("Invalid Input")
  return choice
