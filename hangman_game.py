import random

# Player name
player_name = input("Enter your name: ")

print(f"\n🎮 Welcome {player_name} to Likitha's Smart Hangman Game!")
print("Guess the hidden word and win!")
print("You can also add your own words.\n")

while True:

    # Default words
    default_words = [
        "cricket",
        "mobile",
        "college",
        "computer",
        "friendship"
    ]

    # User custom words
    user_words = input(
        "Enter extra words separated by commas (or press Enter for default words): "
    )

    # Decide words
    if user_words:
        words = user_words.lower().split(",")
        print("✅ Using your custom words!")
    else:
        words = default_words
        print("✅ Using default words!")

    # Difficulty level
    print("\nChoose Difficulty Level:")
    print("1. Easy 😄 (8 chances)")
    print("2. Medium 😎 (6 chances)")
    print("3. Hard 😈 (4 chances)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        max_wrong_guesses = 8
        difficulty = "Easy"

    elif choice == "3":
        max_wrong_guesses = 4
        difficulty = "Hard"

    else:
        max_wrong_guesses = 6
        difficulty = "Medium"

    print(f"\n🎯 Difficulty Selected: {difficulty}")

    # Random word selection
    secret_word = random.choice(words)

    # Hidden word
    guessed_word = ["_"] * len(secret_word)

    # Variables
    wrong_guesses = 0
    guessed_letters = []
    score = 0

    # Game loop
    while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

        print("\n" + "=" * 40)
        print("📝 Word:", " ".join(guessed_word))
        print("❤️ Remaining Chances:",
              max_wrong_guesses - wrong_guesses)
        print("🔤 Used Letters:", guessed_letters)
        print("🏆 Score:", score)

        guess = input(
            "\nEnter a letter or type 'hint': "
        ).lower()

        # Hint feature
        if guess == "hint":

            hidden_letters = []

            for i in range(len(secret_word)):
                if guessed_word[i] == "_":
                    hidden_letters.append(secret_word[i])

            if hidden_letters:
                hint_letter = random.choice(hidden_letters)
                print("💡 Hint Letter:", hint_letter)

            continue

        # Already guessed
        if guess in guessed_letters:
            print("⚠ You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in secret_word:
            print("✅ Correct Guess!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess

            score += 10

        # Wrong guess
        else:
            print("❌ Wrong Guess!")
            wrong_guesses += 1

    # Win condition
    if "_" not in guessed_word:
        print(f"\n🎉 Congratulations {player_name}! You Won!")
        print("✅ The word was:", secret_word)
        print("🏆 Final Score:", score)
        print("🌟 Amazing job! Keep learning and keep shining!")

    # Lose condition
    else:
        print("\n💀 Game Over!")
        print("❌ The correct word was:", secret_word)

    # Play again
    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        print(f"🙏 Thanks for playing, {player_name}!")
        break