import random

def play_game():
    print("Welcome to the game! Choose an option:")
    print("1 - Play with me")
    print("2 - Pass and play")
    print("3 - Exit the game")

    while True:
        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == '1':
            # Implement the game logic here (e.g., a guessing game)
            print("Let's play a game!")
            # game logic here
            # Generate a random number between 1 and 100
            secret_number = random.randint(1, 100)
            attempts = 0

            print("Welcome to the Number Guessing Game!")
            print("I've selected a random number between 1 and 100.")
            print("Can you guess what it is?")

            while True:
                try:
                    guess = int(input("Enter your guess: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                attempts += 1

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

            break
        elif user_choice == '2':
            print("You chose to pass and play.")
            break
        elif user_choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    play_game()
