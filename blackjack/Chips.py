class Chips:
    
  def __init__(self, total=100):
    self.total = total
    self.bet = 0
      
  def win_bet(self):
    self.total += self.bet
  
  def lose_bet(self):
    self.total -= self.bet
  
  def take_bet(self):
    print("You have {} chips.".format(self.total))
    while True:
      try:
        bet = int(input("Place your bet: "))
        if bet < 1: raise ValueError
      except ValueError:
        print("Invalid bet amount")
      else:
        if (bet > self.total):
          print("You don't have enough chips! You have: {}".format(self.total))
        else:
          self.bet = bet
          break
  def player_busts(self):
    print("Player busts!")
    self.lose_bet()

  def player_wins(self):
    print("Player wins!")
    self.win_bet()

  def dealer_busts(self):
    print("Dealer busts!")
    self.win_bet()
      
  def dealer_wins(self):
    print("Dealer wins!")
    self.lose_bet()
      
  def push(self):
    print("Dealer and player tie! Push!")