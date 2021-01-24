'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.'''

'''
input: string
output: string - person who won, and their score
'''
'''
BANANA
B [0:1]
BA [0:2]
BAN [0:3]
BANA [0:4]
BANAN [0:5]
BANANA [0:6]
A [1:2]
AN [1:3]
ANA [1:4]
ANAN [1:5]
ANANA [1:6]
N [2:3]
NA [2:4]
NAN [2:5]
NANA [2:6]
A [3:4]
AN [3:5]
ANA [3:6]
N [4:5]
NA [4:6]
A [5:6]

'''
def minion_game(string):
    # Stuart has to make words starting with consonants.
    # Kevin has to make words starting with vowels.
    stuart_points = 0
    kevin_points = 0
    vowels="AEIOU"
    
    for first_index in range(len(string)):
        if string[first_index] in vowels:
            kevin_points += len(string) - first_index
        else:
            stuart_points += len(string) - first_index
        
    if kevin_points > stuart_points:
        print("Kevin " + str(kevin_points))
    elif stuart_points == kevin_points:
        print("Draw")
    else:
        print("Stuart " + str(stuart_points))
    
if __name__ == '__main__':
    s = input()
    minion_game(s)