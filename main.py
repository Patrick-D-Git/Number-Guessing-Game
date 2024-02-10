# Guessing Number Game
import random


def random_number():
    """randomly picks a number from 1 to 100"""
    number = random.randint(1, 100)
    return number


def check_guess(player_guess, computer_number):
    """checks and compares the user guess to generated guessed number"""
    if player_guess == computer_number:
        print(f"You guessed the number {computer_number}! You won!")
        return True
    elif player_guess > computer_number:
        print("Too high. Guess again.")
        return False
    elif player_guess < computer_number:
        print("Too low. Guess again.")
        return False


EASY = 10
HARD = 5
attempt = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempt = EASY
elif difficulty == "hard":
    attempt = HARD

number_to_guess = int(random_number())

game_finished = False

while not game_finished:

    print(f"You have {attempt} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess: "))

    game_finished = check_guess(user_guess, number_to_guess)
    attempt -= 1

    if attempt == 0:
        print("You've run out of guesses. You lose..")
        game_finished = True
