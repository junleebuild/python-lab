from art import logo
import random
def blackjack():


    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    computer_cards = []

    for i in range(2):
        my_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    dealing = True

    while dealing:

        print(f"    Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        get_another_card = input("Type 'y' to get another card, type 'n' to pass:   ").lower()

        if get_another_card == 'y':
            my_cards.append(random.choice(cards))
            dealing = checking(my_cards, computer_cards)
        else:
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
            dealing = checking_winner(my_cards, computer_cards)


def checking(deck1, deck2):
    if sum(deck1) > 21 and sum(deck2) > 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Both went over. Draw")
        return False
    elif sum(deck1) == 21 and sum(deck2) == 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Both got blackjack. Draw")
        return False
    elif sum(deck1) == 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("You got blackjack. You win")
        return False
    elif sum(deck1) > 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("You went over. You lose")
        return False
    elif sum(deck2) > 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Computer went over. You win")
        return False
    else:
        return True

def checking_winner(deck1,deck2):
    if sum(deck2) > 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Computer went over. You win")
    elif sum(deck2) == 21:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Computer got blackjack. You lose")
    elif sum(deck1) > sum(deck2):
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("You win")
    elif sum(deck1) == sum(deck2):
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("Draw")
    else:
        print(f"    Your cards: {deck1}, current score: {sum(deck1)}")
        print(f"    Computer's cards: {deck2}, current score: {sum(deck2)}")
        print("You lose")
    return False

play_again = True
while play_again:
    play_start = input("Do you want to play a game of Blackjack? Type 'y' pr 'n':   ").lower()
    if play_start == 'y':
        print(logo)
        blackjack()
    else:
        play_again = False




