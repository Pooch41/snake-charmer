from random import randint

NUM_OF_ATTEMPTS = 3


def get_game_output():
    print("Welcome to the Guessing Game!")
    random_number = randint(1, 9)
    guesses = 0
    has_won = False
    while guesses < NUM_OF_ATTEMPTS:
        print(f"\tAttempt number {guesses + 1}")
        while True:
            try:
                guess = int(input("Guess a number between 1 and 9: "))
                if guess < 1 or guess > 9:
                    raise ValueError("Guess must be a number between 1 and 9")
                break
            except ValueError:
                print("Guess must be a number between 1 and 9")

        if guess == random_number:
            print("You guessed it correctly!")
            has_won = True
            break
        guesses += 1

    if has_won:
        print("You won!")
    else:
        print("You lost!")


def main():
    get_game_output()

if __name__ == "__main__":
    main()
