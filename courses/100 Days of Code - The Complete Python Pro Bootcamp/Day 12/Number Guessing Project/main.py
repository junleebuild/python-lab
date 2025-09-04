from art import logo
import random

def guess_the_number(level, number):
    lives = 0

    if level == 'easy':
        lives = 10
    elif level == 'hard':
        lives = 5

    game_over = False
    while not game_over:
        if lives == 0:
            print("You've run out of guesses.")
            game_over = True
        else:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess:    "))
            if guess == number:
                print(f"You got it! The answer was {number}.")
                game_over = True
            elif guess > number:
                print("Too high.\nGuess again.")
                lives -= 1
            elif guess < number:
                print("Too low.\nGuess again.")
                lives -= 1


print(logo)
print("Welcome to the Number Guessing Game!")

continue_game = True
while continue_game:
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()
    guess_the_number(difficulty, answer)
    re_game = input("Do you want to play the game again. Type 'y' to restart or 'n' to quit the game: ").lower()
    if re_game == 'n':
        continue_game = False

