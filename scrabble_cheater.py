#scrabble_cheater.py
# use the characters in RACK to compose words, and more complex is better.


import sys
import scrabble

def valid_word(word, rack):
    #make a copy of the rack for every new word.
    #so we can manupilate it without compromising the original rack.
    available_letters = rack[:]
    
    for letter in word:
        if letter not in available_letters:
            return False
        available_letters.remove(letter)
    
    return True

    
def compute_score(word):
    #calculate the scrabble score for the word
    score = 0
    for letter in word:
        score = score + scrabble.scores[letter]
    return score


#start the program    
if len(sys.argv) < 2:
    print("Usage: scrabble.py [RACK]")
    exit(1)
    
rack = list(sys.argv[1].lower())

valid_words = []

for word in scrabble.wordlist:
    if valid_word(word, rack):
        score = compute_score(word)
        valid_words.append([score, word])

valid_words.sort()

for play in valid_words:
    score = play[0]
    word = play[1]
    print(word + " : "+ str(score))

    