class Hand:

  def __init__(self):
    self.cards = []  # start with an empty list as we did in the Deck class
    self.value = 0   # start with zero value
    self.aces = 0    # add an attribute to keep track of aces
  
  def add_card(self, card):
    if card.rank == 'Ace':
      self.aces += 1
    self.cards.append(card)
    self.value += card.value
  
  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

  def hit(self, deck):
    try:
      self.add_card(deck.deal())
    except AttributeError:
      print("Error: Not hitting from Deck object")
    else:
      self.adjust_for_ace()

  def hit_or_stand(self, deck):
    playing = True

    while True:
      x = input("Hit or Stand? [h/s] ")

      if x[0].lower() == "h":
        self.hit(deck)
      elif x[0].lower() == "s":
        print("Player Stands. Dealer's Turn")
        playing = False
      else:
        print("I don't understand: {}".format(x))
        continue
      break
    return playing
