import random

def main(play_another_game=None):
    welcome_screen = ["THIS IS HANGMAN! The rules are simple, Try to Guess the Word",
               "letter by letter before you run out of attempts! Have Fun!",
               "Also, Let's Try to not let this guy Hang!",
               "The theme of all of the words will be around Junk Food"
               ]

    for sentence in welcome_screen:
        print(sentence, sep='\n')   #this will print the welcome screen and give a line break after each sentence.

    play_another_game = True

    while play_another_game:
        # creating the game loop

        words = ["dasani", "rockstar", "coke", "pepsi", "snickers",
                 "reeses", "candy", "doritos"
                 ]

        selected_word = random.choice(words).lower() #choses one word from the object word. the .lower() is to ensure it is all lowercase
        player_guess = None #variable to hold the number of guesses made
        guessed_letters = [] # creates an array to hold all of the guessed letters so you will not be penalized if you use the same letter twice
        word_guessed = []

        for letter in selected_word:
            word_guessed.append("-") # this will put the dashes at the beginning of the unguessed portion of the word.
        guessing_word = None # will be used to pass the words in the list word_guessed

#all the animations for each stage of the hanging
        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed): #make sure the attempts are greater than 0
            print(("\nYou have {} attempts remaining").format(attempts)) #this puts the attempts value in the {}
            guessing_word = ""
            guessing_word = guessing_word.join(word_guessed)
            print(guessing_word)

            try:    #chapter 7 in launchcode try & except
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha(): # makes sure the input is an alphabet character and not numberical
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input to make sure it is only 1 letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check that the letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass    #pass means skip this.

            guessed_letters.append(player_guess)

            for letter in range(len(selected_word)):
                if player_guess == selected_word[letter]:
                    word_guessed[letter] = player_guess # replace all of the -'s in selected_word that matches the players guesses

            if player_guess not in selected_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no -'s left so this means you guessed the word
            print(("\nYOU DID IT!! I knew you could! {} was the word").format(selected_word)) #winner message
        else: # loop reached zero since guesses are out so the user lost.
            print(("\nAwwww! That sucks! Better luck next time! The word was {}.").format(selected_word))

        print("\nWant to play again?!?!")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
