# Problem Set 2, hangman.py
# Name: Bondar Illya, KM - 93
# Collaborators: ---
# Time spent: ---

# Hangman Game
# ----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

# -----------------------------------
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if not i in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    return "".join(["_ " if i not in letters_guessed else i for i in secret_word])

def get_available_letters(letters_guessed):
    return "".join([i for i in string.ascii_lowercase if i not in letters_guessed])


def hangman(secret_word):
    all = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " ,len(secret_word), " letters long.")
    warnings_left = 3
    guesses_left = 6
    print("You have " + str(warnings_left) + " warnings left")
    vowel = "aeiou"
    letters_guessed = []
    while not guesses_left == 0:
        print("-------------")
        print("You have " + str(guesses_left) + " guesses left")
        print("Available letters: ",get_available_letters(letters_guessed))
        letters_guessed_input = input("Please guess a letter: ").lower()
        lgi = letters_guessed_input
        if len(lgi) > 1 or len(lgi) == 0 or not lgi in all or lgi in letters_guessed:
            warnings_left -= 1
            if warnings_left < 0:
                guesses_left -= 1
            voi1 = "Oops! That is not a valid letter. You have "
            voi2 = "no warnings left so you lose one guess: "
            voi3 = "Oops! You've already guessed that letter. You have "
            if lgi in letters_guessed:
                print(voi3 + str(warnings_left) + " warnings left: " if warnings_left >= 0 else voi3 + voi2
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            print(voi1 + str(warnings_left) + " warnings left: " if warnings_left >=0 else voi1 + voi2
                      ,get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed_input in secret_word:
            letters_guessed.append(lgi)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed) :
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is: ", len(set(secret_word)) * guesses_left)
                break
        elif not letters_guessed_input in secret_word:
            letters_guessed.append(lgi)
            guesses_left -= 1
            if letters_guessed_input in vowel:
                guesses_left -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
    if guesses_left <=0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secret_word)
# -----------------------------------
def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word) or is_word_guessed(other_word,my_word):
        return False
    for i in range(0, len(my_word)):
        if my_word[i] != other_word[i] and not my_word[i] == "_":
            return False
    return True

def show_possible_matches(my_word):
    res = "".join([i +" " for i in wordlist if  match_with_gaps(my_word,i)])
    return res

def hangman_with_hints(secret_word):
    all = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(secret_word), " letters long.")
    warnings_left = 3
    guesses_left = 6
    print("You have " + str(warnings_left) + " warnings left")
    vowel = "aeiou"
    letters_guessed = []
    once = True
    while not guesses_left == 0:
        print("-------------")
        print("You have " + str(guesses_left) + " guesses left")
        print("Available letters: ", get_available_letters(letters_guessed))
        letters_guessed_input = input("Please guess a letter: ").lower()
        lgi = letters_guessed_input
        if letters_guessed_input == "*" and once:
            letters_guessed.append(lgi)
            once = False
            res = print("Possible word matches are:",show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            continue
        if len(lgi) > 1 or len(lgi) == 0 or not lgi in all or lgi in letters_guessed:
            warnings_left -= 1
            if warnings_left < 0:
                if  guesses_left == 1 and  "*" in letters_guessed:
                    guesses_left -= 0
                else:
                    guesses_left -= 1
            voi1 = "Oops! That is not a valid letter. You have "
            voi2 = "no warnings left so you lose one guess if you didn't input '*' and play strong! : "
            voi3 = "Oops! You've already guessed that letter. You have "
            if lgi in letters_guessed:
                print(voi3 + str(warnings_left) + " warnings left: " if warnings_left >= 0 else voi3 + voi2
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            print(voi1 + str(warnings_left) + " warnings left: " if warnings_left >= 0 else voi1 + voi2
                  , get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed_input in secret_word:
            letters_guessed.append(lgi)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is: ", len(set(secret_word)) * guesses_left)
                break
        elif not letters_guessed_input in secret_word:
            letters_guessed.append(lgi)
            if guesses_left == 1 and "*" in letters_guessed:
                guesses_left -= 0
            else:
                guesses_left -= 1
                if letters_guessed_input in vowel and not guesses_left == 1:
                    guesses_left -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
    if guesses_left <= 0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secret_word)
if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)