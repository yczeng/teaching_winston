# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list=list(secret_word)
    for char in secret_word:
        if char in letters_guessed:
            secret_word_list.remove(char)
    return len(secret_word_list)==0


# secret_word='apple'
# letters_guessed=['e','i','k','p','r','s']
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word=[]
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else:
            guessed_word.append('_ ')
    return ''.join(guessed_word)
    
# secret_word='apple'
# letters_guessed=['e','i','k','p','r','s']
# print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters=list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in string.ascii_lowercase:
            available_letters.remove(char)
    return ''.join(available_letters)
    
# letters_guessed=['e','i','k','p','r','s']
# print(get_available_letters(letters_guessed))    

def unique_char(secret_word):
    unique_list=[]
    for idx,char in enumerate(secret_word):
        if idx==0 or not char in secret_word[0:idx]:
            unique_list.append(char)
    return unique_list
            
        
        
def score(secret_word,guesses_remaining):
    return guesses_remaining*len(unique_char(secret_word))

def warning_check(guessed_letter,letters_guessed):
    if not str.isalpha(guessed_letter) or len(guessed_letter)!=1:
        return 1
    elif guessed_letter in letters_guessed:
        return 2
    else:
        return 3


def print_result(letters_guessed,guesses_remaining,):
    print('-'*12)
    print('You have',guesses_remaining,'guesses left.')
    print('Available letters:',get_available_letters(letters_guessed),end='')


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    consonants='bcdfghjklmnpqrstvwxyz'
    vowels='aeiou'
    guesses_remaining=6
    warnings_remaining=3
    letters_guessed=[]
    
    print('Welcome to  the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('You have',warnings_remaining,'warnings left.')
                   
    while not is_word_guessed(secret_word, letters_guessed):
        print_result(letters_guessed, guesses_remaining)
        guessed_letter=str.lower(input('Please guess a letter:'))
        if warning_check(guessed_letter,letters_guessed)==3:
            letters_guessed.append(guessed_letter)
            if letters_guessed[-1] in secret_word:
                print('Good guess:',get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! that letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                if letters_guessed[-1] in consonants:
                    guesses_remaining-=1
                elif letters_guessed[-1] in vowels:
                    guesses_remaining-=2
        else:
            if warnings_remaining!=0:
                warnings_remaining-=1
                if warning_check(guessed_letter, letters_guessed)==1:
                    print('Oops! That is not a valid letter. You have',warnings_remaining,'warnings left:',get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! You've already guessed that letter. You have",warnings_remaining,'warnings left:',get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining-=1
                if warning_check(guessed_letter, letters_guessed)==1:
                    print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) and guesses_remaining>0:
            print('-'*12)
            print('Congratulations, you won!')
            print('Your total score for this game is:',score(secret_word,guesses_remaining))
            break
        elif guesses_remaining<=0: 
            print('-'*12)
            print('Sorry, you ran out of guesses. The word was',secret_word+'.')
            break
        

              


    
    
    
    
    

    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_list=list(''.join(my_word.split()))
    counter1=0
    counter2=0
    target=[]
    if not len(my_word_list)==len(other_word):
        return False
    else:
        for idx,char in enumerate(other_word):
            if my_word_list[idx]==char:
                counter1+=1
            elif my_word_list[idx]=='_':
                counter1+=1
                target.append(idx)
        if counter1==len(other_word):
            for num in target:
                if other_word[num] in get_available_letters(unique_char(my_word)):
                    counter2+=1
            return counter2==len(target)
        else:
            return False        
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num=0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            num+=1
            print(word,end=' ')
    if num==0:
        print('No matches found')        
        
# show_possible_matches('a_ pl_ ')
# show_possible_matches('t_ _ t')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    consonants='bcdfghjklmnpqrstvwxyz'
    vowels='aeiou'
    guesses_remaining=6
    warnings_remaining=3
    letters_guessed=[]
    
    print('Welcome to  the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('You have',warnings_remaining,'warnings left.')
                   
    while not is_word_guessed(secret_word, letters_guessed):
        print_result(letters_guessed, guesses_remaining)
        guessed_letter=str.lower(input('Please guess a letter:'))
        if guessed_letter=='*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print('')
        else:    
            if warning_check(guessed_letter,letters_guessed)==3:
                letters_guessed.append(guessed_letter)
                if letters_guessed[-1] in secret_word:
                    print('Good guess:',get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! that letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                    if letters_guessed[-1] in consonants:
                        guesses_remaining-=1
                    elif letters_guessed[-1] in vowels:
                        guesses_remaining-=2
            else:
                if warnings_remaining!=0:
                    warnings_remaining-=1
                    if warning_check(guessed_letter, letters_guessed)==1:
                        print('Oops! That is not a valid letter. You have',warnings_remaining,'warnings left:',get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! You've already guessed that letter. You have",warnings_remaining,'warnings left:',get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining-=1
                    if warning_check(guessed_letter, letters_guessed)==1:
                        print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) and guesses_remaining>0:
            print('-'*12)
            print('Congratulations, you won!')
            print('Your total score for this game is:',score(secret_word,guesses_remaining))
            break
        elif guesses_remaining<=0: 
            print('-'*12)
            print('Sorry, you ran out of guesses. The word was',secret_word+'.')
            break
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)