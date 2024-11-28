'''
Created on October 3 2024
@author:   Aidan Miller
Pledge:    _______________________
CS115 - Hw 2
'''
from functools import reduce       
import sys
sys.setrecursionlimit(10000)
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    if not scorelist:         # base case: the list is empty
        return False
    elif scorelist[0] == letter: # check if current element is the one we're looking
        return True
    else:                              # if current element is a list
        return findList(scorelist[1:], letter) or findList(scorelist[1:], letter)


def wordScore(S, scorelist):
    if not scorelist:
        return False
    else:
        return reduce(map((lambda x, y: x + y), letterscore(S[1:], scorelist)), len(S))

def skibidiWords(letters, word):
    if letters = []:
        return True
    elif len(letters) < len(word):
        return False
    elif letters[0] in word:
        skibidayIndex = SkibidiWords(letters[0], word)
        return skibidiWords(
            letters[1:], word[:letterIndex] + word[letterIndex + 1:]
        )
    else:
        if len(letters) > len(word):
            return SkibidiWords(letters[1:], word)
        else:
            return False

def scoreList(Rack):
    wordlist = filter(lambda word: skibidiWords(word, Rack), Dictionary)
    return list(map(lambda word: [word, wordScore(word, scrabbleScore)], validWords))


    
def bestWord(Rack):
    pwod = scoreList(Rack)
    if not pwod:
        return ["", 0]

    return reduce(
        lambda best, word: word if word[1] > best[1] else best, pwod










    
