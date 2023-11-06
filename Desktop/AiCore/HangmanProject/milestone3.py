import random

word_list = ["guava", "mango", "banana", "watermelon", "apples"]

word = random.choice(word_list)

print(word)

characters_random_word = list(word)
# or characters_random_word = [char for char in word]

print(characters_random_word)


def check_guess(guess):
    if guess in characters_random_word:
        print(f"Good guess! the letter {guess} is in the word")
    else:
        print(f"Sorry, the letter {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Guess a single letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()