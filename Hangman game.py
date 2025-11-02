import random

# Step 1: Predefined word list
word_list = ["apple", "banana", "grape", "orange", "peach"]

# Step 2: Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Step 3: Game loop
print("🎯 Welcome to Hangman!")
print("_ " * len(secret_word))

while incorrect_guesses < max_attempts:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("💀 Game over! The word was:", secret_word)
