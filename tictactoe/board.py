def spc(s):
    return ' '+s+' '

def display_board(board):
    print()
    print(spc(board[1])+'|'+spc(board[2])+'|'+spc(board[3]))
    print('---|---|---')
    print(spc(board[4])+'|'+spc(board[5])+'|'+spc(board[6]))
    print('---|---|---')
    print(spc(board[7])+'|'+spc(board[8])+'|'+spc(board[9]))
    print()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    def chk(i):
        return board[i] == mark
    
    # rows
    if (chk(1) and chk(2) and chk(3)) or \
        (chk(4) and chk(5) and chk(6)) or \
        (chk(7) and chk(8) and chk(9)):
        return True
    
    # cols
    if (chk(1) and chk(4) and chk(7)) or \
        (chk(2) and chk(5) and chk(8)) or \
        (chk(3) and chk(6) and chk(9)):
        return True
    
    # diags
    if (chk(1) and chk(5) and chk(9)) or \
        (chk(3) and chk(5) and chk(7)):
        return True
    return False


def space_check(board, position):
  try:
    if position == 0: raise IndexError

    if board[position] == ' ':
      return True
    else:
      print("That space is taken.")
      return False
  except IndexError:
    print("That's an invalid space!")
    return False

def full_board_check(board):
  for i in board:
    if i == ' ':
      return False
  return True
