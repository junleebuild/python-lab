from art import logo, vs
from game_data import data
import random

data_list = data

def main():
    my_point = 0
    playing = True
    while playing:

        A = random.choice(data_list)
        data_list.remove(A)
        B = random.choice(data_list)
        data_list.remove(B)
        choice_map = {
            "A": A,
            "B": B
        }
        print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
        print(vs)
        print(f"Compare B: {B['name']}, {B['description']}, {B['country']}")
        decision = input("Who has more followers? Type 'A' or 'B':  ").upper()

        print("\n" * 20)
        print(logo)

        if choice_map[decision]['follower_count'] > choice_map['A' if decision == 'B' else 'B']['follower_count']:
            my_point += 1
            print(f"You're right! Current score: {my_point}.")

        else:
            print(f"Sorry, that's wrong. Final score: {my_point}")
            playing = False


print(logo)
main()

