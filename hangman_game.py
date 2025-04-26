import random

# List of words to choose from
words_list = ["python", "hangman", "challenge", "programming", "adventure", "developer", "algorithm"]

# Randomly select a word from the list
selected_word = random.choice(words_list)

# Initialize variables
guessed_letters = []  # To store the letters guessed by Aditya
attempts_left = 6     # Limit on incorrect guesses

# Function to display the current state of the word
def display_current_word():
    display = ""
    for letter in selected_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Welcome message
print("🎯 Welcome to Hangman, Aditya Vatsya! 🎯")
print("Guess the word one letter at a time.")
print(f"You have {attempts_left} incorrect guesses allowed.\n")

# Main game loop
while attempts_left > 0:
    print("Word:", display_current_word())
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try a different one.\n")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the selected word
    if guess in selected_word:
        print("✅ Good job! That letter is in the word.\n")
    else:
        attempts_left -= 1
        print(f"❌ Sorry, that letter is not in the word. Attempts left: {attempts_left}\n")

    # Check if Aditya has guessed the full word
    if all(letter in guessed_letters for letter in selected_word):
        print("\n🎉 Congratulations Aditya! You guessed the word correctly:", selected_word)
        break
else:
    # Runs if the while loop ends without a break (Aditya lost)
    print("\n💔 Sorry Aditya, you're out of attempts!")
    print("The word was:", selected_word)

print("\nThanks for playing, Aditya! 👋")
