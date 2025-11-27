import random

def title():
    print("Welcome to matt's super amazing Blackjack game!!!")
    print("-------------------------------------------------")
    print("If you win the payout is a whopping X1.5 your bet!!!")
    print("")



def get_deck():
    deck = []
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["\u2660", "\u2665\uFE0F", "\u2666\uFE0F", "\u2663"]
    for rank in ranks:
        for suit in suits:
            deck.append((suit, rank))
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




def main():
    title()
    deck = get_deck()
    player_hand(deck)

if __name__ == "__main__":
    main()