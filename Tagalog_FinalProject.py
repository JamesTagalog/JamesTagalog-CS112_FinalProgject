import random

def guess_number(player):
    secret_number = random.randint(1, 100)
    attempts = 0
    print(f"\nWelcome, Player {player}! I'm thinking of a number between 1 and 100.")

    while attempts < 10:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Player {player}! You guessed the right number {secret_number} in {attempts} attempts. Congratulations!")
                return True

        except ValueError:
            print("Please enter a valid number.")

    print(f"Player {player}, you've reached the guess limit. The correct number was {secret_number}.")
    return False

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

while True:
    result_player_1 = guess_number(1)
    result_player_2 = guess_number(2)

    if result_player_1 and result_player_2:
        print("\nResults:")
        print("---------------------------------------------------")
        print("Player 1 and Player 2 both guessed the correct number!")
        print("It's a draw!")
    elif result_player_1:
        print("\nResults:")
        print("---------------------------------------------------")
        print("Player 1 wins! Player 2 did not guess the correct number.")
    elif result_player_2:
        print("\nResults:")
        print("---------------------------------------------------")
        print("Player 2 wins! Player 1 did not guess the correct number.")
    else:
        print("\nResults:")
        print("---------------------------------------------------")
        print("Both players reached the guess limit. It's a draw!")

    if not play_again():
        print("Thanks for playing!")
        break
