import random

def hangman():
    words = ["python", "computer", "program", "keyboard", "code"]

    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    print("Guess the word, one letter at a time.")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        guess = input("Enter a letter: ").lower()

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess

            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\nYou win! The word was:", word)
    else:
        print("\nGame over! The word was:", word)


hangman()