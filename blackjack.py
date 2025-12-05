import random
import db



def title():
    print("Welcome to matt's super amazing Blackjack game!!!")
    print("-------------------------------------------------")
    print("You can win the BlackJack payout of a whopping X1.5 your bet!!!")
    print("")


def balance_manage():
    balance = db.read_money()
    if balance <= 5:
        buy = input("Your balance has gone done to or below 5. Would you like to buy more?: ")
        if buy == "yes":
            while True:
                try:
                    more = float(input("How many chips would you like to buy?: "))
                    balance += more
                    return balance
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    continue
        elif buy == "no":
            print("Ok have a good day.")
            return balance
    return balance


def bet_amount(balance):
    while True:
        try:
            bet = float(input("How much would you like to bet? (min: 5 max: 1000): "))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    while True:
        if bet >= 5 or bet <= 1000:
            if bet <= balance:
                return bet

            else:
                print(f"Bet must be within your balance. Your current balance is {balance}.")
        else:
            print("Please bet within the limits of 5 and 1000.")
        



def get_deck():
    deck = []
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [(1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ["\u2660", "\u2665\uFE0F", "\u2666\uFE0F", "\u2663"]
    for suit in suits:
        for value, rank in enumerate(ranks):
            deck.append([suit, rank, values[value]])
    return deck


def player_hand(deck):
    player = []
    deal_card(deck, player, is_player=True)
    return player


def dealer_points(dealer):
    dealer_total_points = 0
    aces = 0
    for card in dealer:
        if isinstance(card[2], int) and card[1] == "Ace":
            dealer_total_points += card[2]
            if card[2] == 11:
                aces += 1
        else:
            rank = card[1]
            if rank == "Ace":
                aces += 1
                dealer_total_points += 11
            elif rank in ["Jack", "Queen", "King"]:
                dealer_total_points += 10
            else:
                dealer_total_points += int(rank)
    
    while dealer_total_points > 21 and aces > 0:
        dealer_total_points -= 10
        aces -= 1
    
    return dealer_total_points



def player_points(player):
    player_total_points = 0
    aces = 0
    for card in player:
        if isinstance(card[2], int) and card[1] == "Ace":
            player_total_points += card[2]
            if card[2] == 11:
                aces += 1
        else:
            rank = card[1]
            if rank == "Ace":
                aces += 1
                player_total_points += 11
            elif rank in ["Jack", "Queen", "King"]:
                player_total_points += 10
            else:
                player_total_points += int(rank)
    
    while player_total_points > 21 and aces > 0:
        player_total_points -= 10
        aces -= 1
    
    return player_total_points


def dealer_hand(deck):
    dealer = []
    deal_card(deck, dealer, is_player=False)
    return dealer


def deal_card(deck, hand, is_player=False):
    rand_int = random.randint(0, len(deck)-1)
    card = deck.pop(rand_int)
    hand.append(card)
    if card[1] == "Ace":
        if is_player:
            while True:
                choice = input("You drew an Ace. Choose its value (1 or 11): ").strip()
                if choice in ("1", "11"):
                    card[2] = int(choice)
                    break
                else:
                    print("Please enter 1 or 11.")
        else:
            other = hand[:-1]
            if other:
                other_total = dealer_points(other)
            else:
                other_total = 0
            if other_total + 11 <= 21:
                card[2] = 11
            else:
                card[2] = 1


def display_hand(hand, name, hide_first=False):
    if hide_first and len(hand) > 1:
        second = hand[1]
        print(f"{name}'s hand: [Hidden] [{second[0]} {second[1]}]")
    else:
        cards_str = " ".join([f"[{card[0]} {card[1]}]" for card in hand])
        if name.lower().startswith("your"):
            total = player_points(hand)
        else:
            total = dealer_points(hand)
        print(f"{name} hand: {cards_str} (Total: {total})")


def player_turn(deck, hand):
    while True:
        total = player_points(hand)

        if total == 21:
            print(f"You have {total}. Automatic stand.")
            return True

        if total > 21:
            print(f"You bust with {total}!")
            return False

        display_hand(hand, "Your")
        action = input("Do you want to hit or stand? (H/S): ").strip().upper()
        if action == "H":
            deal_card(deck, hand, is_player=True)
            print("")
            continue
        elif action == "S":
            print(f"You stand with {total}")
            return True
        else:
            print("Please enter H or S.")


def dealer_turn(deck, hand):
    display_hand(hand, "Dealer")
    while dealer_points(hand) < 17:
        print(f"Dealer hits (Dealer total: {dealer_points(hand)})")
        deal_card(deck, hand, is_player=False)
    dealer_total = dealer_points(hand)
    print(f"Dealer stands with {dealer_total}")
    return dealer_total



def main():
    title()
    while True:
        balance = balance_manage()
        bet = bet_amount(balance)
        deck = get_deck()
        player_hands = player_hand(deck) + player_hand(deck)
        dealer_hands = dealer_hand(deck) + dealer_hand(deck)

        print(f"Your balance is {balance}")
        print(f"Your bet is {bet}")
        print("")

        display_hand(player_hands, "Your")
        display_hand(dealer_hands, "Dealer", hide_first=True)
        print("")

        player_total = player_points(player_hands)
        dealer_total = dealer_points(dealer_hands)

        if player_total == 21 and len(player_hands) == 2:
            if dealer_total == 21 and len(dealer_hands) == 2:
                print("Both you and the dealer have blackjack! It's a push.")
            else:
                print("BLACKJACK! You win!")
                balance += bet * 1.5
        elif dealer_total == 21 and len(dealer_hands) == 2:
            print("Dealer has blackjack! You lose.")
            balance -= bet
        else:
            player_not_busted = player_turn(deck, player_hands)

            if player_not_busted:
                print("")
                dealer_turn(deck, dealer_hands)

                player_total = player_points(player_hands)
                dealer_total = dealer_points(dealer_hands)

                print("")
                display_hand(player_hands, "Your")
                display_hand(dealer_hands, "Dealer")
                print("")

                if dealer_total > 21:
                    print("Dealer busted! You win!")
                    balance += bet * 0.5
                elif player_total > dealer_total:
                    print("You win!")
                    balance += bet * 0.5
                elif dealer_total > player_total:
                    print("Dealer wins.")
                    balance -= bet
                else:
                    print("Push! It's a tie.")
            else:
                balance -= bet
        
        db.write_money(balance)
        
        play_again = input("Would you like to play another hand? (yes/no): ")
        if play_again.lower() != "yes":
            print(f"Thanks for playing! Final balance: {balance}")
            break
        
if __name__ == "__main__":
    main()