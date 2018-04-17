import random
# import string

"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
movie_list = ["Love in basketball", "Vampire diaries", "Insidious", "Split", "The originals", "Get rich or die trying",
              "Jumanji 2", "chucky", "Anabelle", "The perfect game"]

movie = movie_list[random.randint(0, len(movie_list) - 1)]
print(movie)
letters_guessed = []
guess_left = 10

current_guess = ""
while guess_left > 0 and current_guess != "quit":
    # Prints out the output
    output = []
    for letter in movie:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(list(output)))

    # Takes a guess and adds it to letters guessed
    current_guess = input("type a letter:")
    letters_guessed.append(current_guess)
    print(letters_guessed)

    # Handles incorrect guesses
    if current_guess not in movie:
        guess_left -= 1
        print("%d guess left" % guess_left)
