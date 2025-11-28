import random

def title():
    print("Welcome to matt's super amazing Blackjack game!!!")
    print("-------------------------------------------------")
    print("If you win the payout is a whopping X1.5 your bet!!!")
    print("")



def get_deck():
    deck = []
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ["\u2660", "\u2665\uFE0F", "\u2666\uFE0F", "\u2663"]
    for suit in suits:
        for value, rank in enumerate(ranks):
            deck.append([suit, rank, values[value]])
    print(deck)
    return deck


def player_hand(deck):
    player = []
    rand_int = random.randint(1, len(deck))
    chosen_card = deck[rand_int]
    player.append(chosen_card)
    deck.pop(rand_int)
    print(player)
    print(deck)

def player_points(chosen_card, player):
    total_points = 0
    for 

def dealer_hand(deck):
    dealer = []
    rand_int = random.randint(1, len(deck))
    chosen_card = deck[rand_int]
    dealer.append(chosen_card)
    deck.pop(rand_int)
    print(dealer)
    print(deck)


def main():
    title()
    deck = get_deck()
    player_hand(deck)
    dealer_hand(deck)
if __name__ == "__main__":
    main()