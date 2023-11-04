import random

# Intitliase the list of items, in this case my favourite fruits 

word_list = ["guava", "mango", "banana", "watermelon", "apples"]

print(word_list)

# Generate a random item from the list 

word = random.choice(word_list)

print(word)

# Create a input variable where the user guesses one letter

guess = input("Guess a single letter: ").lower()

# Check if the guessed letter is in fact a strong and is one letter
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input!, please enter a letter")

