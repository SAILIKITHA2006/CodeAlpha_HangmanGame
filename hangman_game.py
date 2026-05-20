import random

# List of words
words = ["cricket", "mobile", "college", "computer", "friendship"]

# Random word selection
secret_word = random.choice(words)

# Create hidden word with underscores
guessed_word = ["_"] * len(secret_word)

# Maximum wrong guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Store guessed letters
guessed_letters = []

# Score
score = 0

# Welcome message
print("🎮 Welcome to Likitha's Hangman Challenge!")
print("Guess the hidden word and win the game!")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Remaining chances:", max_wrong_guesses - wrong_guesses)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check repeated letter
    if guess in guessed_letters:
        print("⚠ You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Correct Guess!")
        score += 10
        print("Score:", score)

        # Reveal letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    # Wrong guess
    else:
        print("❌ Wrong Guess!")
        wrong_guesses += 1

# Winning condition
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You Won!")
    print("The word was:", secret_word)
    print("Final Score:", score)

# Losing condition
else:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)

# Play again option
play_again = input("\nDo you want to play again? (yes/no): ")

if play_again.lower() == "yes":
    print("Restart the program to play again!")
else:
    print("Thanks for playing!")