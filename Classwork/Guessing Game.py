import random as rand

def guessing_game(num_of_guesses):
    lives = num_of_guesses;
    to_guess = rand.randint(1, 6)
    print("""Welcome to the guessing game!
    Guess the number between 1 and 6!
    If you guess wrong 3 times, you lose!
    You may be saved if you roll 5 or 6 on the life-saver dice!""")
    while lives > 0:
        guess = int(input("Guess a number between 1 and 6: "))
        if guess == to_guess:
            print(".°˖✧ Correct! You win! ✧˖°.")
            break
        else:
            lives -= 1
            print("Incorrect!")
            life_saver = rand.randint(1, 6)

            if life_saver >= 5:
                print(f"You are saved! You rolled {life_saver}. Over 5 or 6!")
                lives += 1
            else:
                print(f"You are not saved! You rolled {life_saver}!")

    if lives == 0:
        print(f"You lose! The number was {to_guess}.")


def main():
    num_of_guesses = 3 #From req doc
    guessing_game(num_of_guesses)

if __name__ == "__main__":
    main()