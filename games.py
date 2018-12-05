game_list = {
  "1": "Tic-tac-toe",
  "2": "Blackjack"
}

def pick_game():
  while True:
    ans = input()
    try:
      print(f"You picked: {game_list[ans]}")
      return ans
    except KeyError:
      print("We don't have that one yet...")
      print("Try again!")

def play_tictactoe():
  from tictactoe import tictactoe
  tictactoe.game_loop()

def play_blackjack():
  from blackjack import blackjack
  blackjack.game_loop()

if __name__ == '__main__':
  while True:
    print("\nEnter a number to pick a game to play:")
    for game in game_list:
      print(f"\t[{game}]: {game_list[game]}")

    picked = pick_game()
    if picked == '1':
      play_tictactoe()
    elif picked == '2':
      play_blackjack()
    
    again = input("Do you want to play a different game? [Y/N]: ")
    if again.lower() == "y":
      continue
    else:
      break