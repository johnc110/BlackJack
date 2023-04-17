import requests
import json
import pprint

deck_id = ""

# Get a new deck of cards
def new_deck():
    global deck_id
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    deck = json.loads(response.text)
    deck_id = deck['deck_id']

# Draw a card from the deck
def draw_card():
    global deck_id
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
    response = requests.get(url)
    card = json.loads(response.text)['cards'][0]
    return card

# Calculate the value of a hand
def hand_value(hand):
    value = 0
    for card in hand:
        if card['value'] in ['JACK', 'QUEEN', 'KING']:
            value += 10
        elif card['value'] == 'ACE':
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        else:
            value += int(card['value'])
    return value

# Play a game of Blackjack
def play_game():
    # Get a new deck of cards
    new_deck()

    # Deal the initial hands
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    # Show the player's hand and ask for their move
    print("Player's hand:", player_hand)
    while True:
        move = input("Hit or stand? ")
        if move.lower() == 'hit':
            player_hand.append(draw_card())
            print("Player's hand:", player_hand)
            if hand_value(player_hand) > 21:
                print("Player busts!")
                return -1
        else:
            break

    # Dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    # Determine the winner
    print("Dealer's hand:", dealer_hand)
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busts! Player wins!")
        return 1
    elif dealer_value > player_value:
        print("Dealer wins!")
        return -1
    elif player_value > dealer_value:
        print("Player wins!")
        return 1
    else:
        print("Tie!")
        return 0

# Play a game of Blackjack with user input
while True:
    play_again = input("Do you want to play a game of Blackjack? (Y/N) ")
    if play_again.lower() == 'y':
        result = play_game()
        if result == 1:
            print("Congratulations! You won!")
        elif result == 0:
            print("It's a tie!")
        else:
            print("Sorry, you lost.")
    else:
        break






