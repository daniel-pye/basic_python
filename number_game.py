import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = 5
    while True:
        # get a guess from the player
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}.".format(secret_num))
                break
            elif guess < secret_num:
                print("That's not it! You guessed too low.")
                guesses -= 1
                if guesses == 0:
                    print("You're out of guesses. The number was {}. Better luck next time.".format(secret_num))
                    break
                print("You have {} guesses left. Try again.".format(guesses))
            else:
                print("That's not it! You guessed too high.")
                guesses -= 1
                if guesses == 0:
                    print("You're out of guesses. The number was {}. Better luck next time.".format(secret_num))
                    break
                print("You have {} guesses left. Try again.".format(guesses))

game()
play_again = input("Would you like to play again? y/n ")
if play_again == 'y':
    game()
else:
    print("Thanks for playing!")
