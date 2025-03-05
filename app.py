import random

def get_difficulty():
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts_left = get_difficulty()
    
    print(f"\nGreat! You have {attempts_left} chances to guess the correct number. Let's start the game!")
    
    attempts = 0
    
    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            attempts_left -= 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Incorrect! The number is greater than", guess)
            elif guess > secret_number:
                print("Incorrect! The number is less than", guess)
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                return
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print(f"Sorry, you have run out of attempts. The correct number was {secret_number}.")
    
if __name__ == "__main__":
    number_guessing_game()
