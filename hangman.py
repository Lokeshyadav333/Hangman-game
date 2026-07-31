import random

def display_word(word, guessed_letters):
    """
    Displays the secret word with letters revealed if they have been guessed,
    and underscores for those that haven't.
    """
    displayed = []
    for letter in word:
        if letter.lower() in guessed_letters:
            displayed.append(letter.upper())
        else:
            displayed.append("_")
    return " ".join(displayed)

def play_hangman():
    # Predefined list of words
    words = ["apple", "tiger", "chair", "house", "pizza"]
    
    # Select a random word
    secret_word = random.choice(words)
    
    # Store guessed letters (in lowercase for case-insensitive matching)
    guessed_letters = set()
    
    # Incorrect guesses tracker
    incorrect_guesses = set()
    
    # Maximum incorrect attempts allowed
    max_attempts = 6
    
    print("====================================")
    print("        WELCOME TO HANGMAN!         ")
    print("====================================")
    
    while len(incorrect_guesses) < max_attempts:
        attempts_left = max_attempts - len(incorrect_guesses)
        
        # Display status
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        if incorrect_guesses:
            print(f"Wrong Letters: {', '.join(sorted([letter.upper() for letter in incorrect_guesses]))}")
        print(f"Attempts Left: {attempts_left}")
        
        # Prompt user input
        guess = input("Enter a letter: ").strip()
        
        # Input Validation (FR3)
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single alphabetic letter.")
            continue
            
        guess_lower = guess.lower()
        
        # Check if already guessed (FR6)
        if guess_lower in guessed_letters or guess_lower in incorrect_guesses:
            print("You already guessed that letter.")
            continue
            
        # Check if correct (FR4 & FR5)
        if guess_lower in secret_word.lower():
            guessed_letters.add(guess_lower)
            print(f"Good guess! '{guess.upper()}' is in the word.")
        else:
            incorrect_guesses.add(guess_lower)
            print(f"Wrong Letter: {guess.upper()}")
            
        # Check Win Condition (FR7)
        # Check if all letters in secret_word are in guessed_letters
        word_letters = set(secret_word.lower())
        if word_letters.issubset(guessed_letters):
            print(f"\nWord: {display_word(secret_word, guessed_letters)}")
            print("\nCongratulations!")
            print("You Won!")
            print(f"The Word is {secret_word.upper()}")
            return
            
    # Lose Condition (FR8)
    print("\nAttempts Left: 0")
    print("\nGame Over")
    print(f"The correct word was {secret_word.upper()}")

if __name__ == "__main__":
    play_hangman()
