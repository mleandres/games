from blackjack.Deck import Deck
from blackjack.Chips import Chips
from blackjack.Hand import Hand

def show_some(player,dealer):
  print("\nDealer's Hand:")
  print(" <card hidden>")
  print('',dealer.cards[1])  
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
  print("\nDealer's Hand:", *dealer.cards, sep='\n ')
  print("Dealer's Hand =",dealer.value)
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
  print("Player's Hand =",player.value)

def game_loop():
  chips = Chips()
  playing = True

  while True:

    print("\nWelcome to BlackJack, my dude!")

    # setup
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    chips.take_bet
    
    show_some(player, dealer)

    # start playing
    while playing:
    
      playing = player.hit_or_stand(deck)
      
      show_some(player, dealer)
      
      if player.value > 21:
        chips.player_busts()
        break

    if player.value <= 21:
        
      while dealer.value < 17:
        dealer.hit(deck)
      
      show_all(player, dealer)

      if dealer.value > 21:
        chips.dealer_busts()
      elif dealer.value > player.value:
        chips.dealer_wins()
      elif dealer.value < player.value:
        chips.player_wins()
      else:
        chips.push()

    print(f"Your chip total is: {chips.total}.")
    
    if chips.total < 1:
      print("Player has run out of chips :(")
      break
    
    ans = input("Do you want to play again? [Y/N]: ")
    if ans[0].lower() == "y":
      playing = True
      continue
    else:
      break

  print("Ok see ya")

if __name__ == '__main__':
  game_loop()