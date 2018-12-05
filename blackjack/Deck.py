import random
from blackjack.Card import Card

suits = ('Hearts','Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    
  def __init__(self):
    self.deck = []  # start with an empty list
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))
  
  def __str__(self):
    result = ""
    for card in self.deck:
      result += str(card) + "\n"
    return result

  def shuffle(self):
    random.shuffle(self.deck)
      
  def deal(self):
    return self.deck.pop()