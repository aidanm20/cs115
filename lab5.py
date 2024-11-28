############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 5
#
############################################################
# Imports
import string
import operator
import pickle

# --------------------------------------------------------------------------------
# PRE: needs a dictionary with word:count pair
# POST: returns sorted dictionary
# PURPOSE: receives a dictionary and returns a sorted version
def sortDictionaryAlphabetically(bookDict):
    return sorted(bookDict.keys())


# --------------------------------------------------------------------------------
# PRE: needs a dictionary with word:count pair
# POST: a dictionary of word-count pairs with the top 10 value scores.
# PURPOSE: get a dictionary and sort it by count values
def top10WordCounts(bookDict):
    return dict(sorted(bookDict.items(), key = lambda item: item[1], reverse=True)[:10])

# --------------------------------------------------------------------------------
# PRE: needs dictionary and a word
# POST: # of times a word occurred. If not exists, return -1
# PURPOSE: displays the count of a word in a dictionary
def searchWord(word, bookDict):
    if word not in bookDict:
        return -1
    else:
        return bookDict[word]



# --------------------------------------------------------------------------------
# PRE: a dictionary with word:count pairs
# POST: a dictionary words with count higher than 50
# PURPOSE: using higher order functions with dictionaries
def higherThan50(bookDict):
    return dict(filter(lambda item: item[1] > 50, bookDict.items()))
        
# -------------------------------------------------------------------------------

def testSearchWord(bookDict):
    assert searchWord("able", bookDict) == 11
    assert searchWord("protagoras", bookDict) == 2
    assert searchWord("reason", bookDict) == 13
    assert searchWord("list", bookDict) == -1
    assert searchWord("ruse", bookDict) == -1
    assert searchWord("facebook", bookDict) == -1

def testHigherThan50(bookDict):
    with open('higher50.pickle', 'rb') as handle:
        higher50 = pickle.load(handle)
    assert higherThan50(bookDict) == higher50

def testTop10WordCounts(bookDict):
    with open('top10.pickle', 'rb') as handle:
        top10 = pickle.load(handle)
    assert top10WordCounts(bookDict) == top10


# --------------------------------------------------------------------------------
def main():
    # Load dictionary
    bookDict = {}
    with open('dictionary.pickle', 'rb') as handle:
        bookDict = pickle.load(handle)
    
    # sort dictionary alphabet
    alphaDict = sortDictionaryAlphabetically(bookDict)
    
    testSearchWord(bookDict)
    testHigherThan50(bookDict)
    testTop10WordCounts(bookDict)

main()
