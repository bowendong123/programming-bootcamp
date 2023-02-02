import random

def game_menu():
    print("Number Guessing Game!")
    answer = random.randint(1,100)
    while True:
        guess = input("Guess the number between 1 and 100: ")
        while True:
            guessValidity = validate_user_guess(guess)
            if guessValidity == "Valid":
                break
        win = check_for_win(int(guess),answer)
        if win == True:
            break


def validate_user_guess(guess):
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input, please ensure your guess is an integer")
        return "Invalid"

    if guess % 1 != 0:
        print("Invalid input, please ensure your guess is an integer")
        return "Invalid"
    elif guess < 1 or guess > 100:
        print("Invalid input, please ensure your guess is between 1 and 100")
        return "Invalid"
    else:
        return "Valid"

def check_for_win(guess,answer):
    if guess < answer:
        print("Higher")
    elif guess > answer:
        print("Lower")
    elif guess == answer:
        print("Congrats! You guessed the number correctly!")
        return True


game_menu()
