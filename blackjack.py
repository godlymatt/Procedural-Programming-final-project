import random

def title():
    print("Welcome to matt's super amazing Blackjack game!!!")
    print("-------------------------------------------------")
    print("If you win the payout is a whopping X1.5 your bet!!!")
    print("")



def get_deck():
    deck = []
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [(1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ["\u2660", "\u2665\uFE0F", "\u2666\uFE0F", "\u2663"]
    for suit in suits:
        for value, rank in enumerate(ranks):
            deck.append([suit, rank, values[value]])
    print(deck)
    return deck


def read_money():
    with open("money.txt", "r") as infile:
        for line in infile:
            new_line = line
            money = float(new_line)
            return money
        


def write_money(balance):
    with open("money.txt", "w") as outfile:
        outfile.write(str(balance))


def player_hand(deck):
    player = []
    rand_int = random.randint(1, len(deck)-1)
    chosen_card = deck[rand_int]
    player.append(chosen_card)
    deck.pop(rand_int)
    print(player)
    print(deck)
    return player


def dealer_points(dealer):
    dealer_total_points = 0
    aces = 0
    for card in dealer:
        card_value =card[2]
        if card[1] == "Ace":
            aces += 1
            dealer_total_points += 1
        else:
            dealer_total_points += card_value
        while aces > 0 and dealer_total_points + 10 <= 21:
            dealer_total_points += 10
            aces -= 1
        return dealer_total_points



def player_points(player):
    player_total_points = 0
    for card in player:
        if card[1] == "Ace":
            if player_total_points <= 10:
                while True:
                    ace_choice = input("You have drawn an ace. Would you like it to be 1 or 11 points?: ")
                    if ace_choice == "1" or ace_choice == "11":
                        player_total_points += int(ace_choice)
                        break
                    else:
                        print("You must pick between 1 and 11. Try again.")
            else:
                player_total_points += 1
        else:
            player_total_points += card[2]
    return player_total_points


def dealer_hand(deck):
    dealer = []
    rand_int = random.randint(1, len(deck)-1)
    chosen_card = deck[rand_int]
    dealer.append(chosen_card)
    deck.pop(rand_int)
    print(dealer)
    print(deck)
    return dealer


def main():
    title()
    deck = get_deck()
    player_hand(deck)
    dealer_hand(deck)
if __name__ == "__main__":
    main()