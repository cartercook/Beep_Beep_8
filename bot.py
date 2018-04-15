import random
from random import randint
import numpy
import requests
import tweepy

from secrets import *

#TODO: tweet every 3 hours

# ---------- CLASS DECLARATIONS ----------

# contains beeps
class Word:
    def __init__(self, string, max):
        self.string = string
        self.max = max

# ---------- VARIABLE DECLARATIONS ----------

beeps = [
    # in order of probability
    Word("beep", 3),
    Word("boop", 3),
    Word("bleep", 3),
    Word("bwoop", 2),
    Word("woop", 1),
    Word("bweep", 1),
    Word("deet", 2),
    Word("doot", 3),
    Word("weeo", 1),
    Word("bop", 2),
    Word("bawoop", 2),
    Word("badeep", 2),
    Word("badoop", 2)
]

rares = [
    Word("Poe[!/?]", 1) #(1/100)
]

sounds = [
    Word("*bonk*", 3),
    Word("*ding*", 2),
    Word("*whir*", 3),
    Word("*zzzt*", 1),
]

# ---------- MAIN ----------

# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)  # create an API object


def tweet():
    # create list of all beeps and sounds, multiplied by max use
    allBeeps = generateExpandedList(beeps)
    allWords = allBeeps + generateExpandedList(sounds)

    # start with random word
    phrase = [selectRandomWord(allWords)]

    dieRoll = randint(0, 2)

    if dieRoll >= 1:
        # add another word
        phrase.append(selectRandomWord(allWords))

    if dieRoll is 2:
        # add another word
        phrase.append(selectRandomWord(allWords))


    # Shuffle array
    random.shuffle(phrase)

    # Capitalize first letter
    phrase[0].title()

    # Add spaces between words
    phrase = ' '.join(phrase)

    # Update the authenticated user's status
    api.update_status(status=phrase)


# ---------- HELPER FUNCTIONS ----------

# remove and return a random beep from wordList
def selectRandomWord(wordList):
    # TODO: probability distribution
    beep = random.choice(wordList)
    wordList.remove(beep)
    return beep


def generateExpandedList(wordList):
    expandedList = []
    for word in wordList:
        expandedList += [word.string] * word.max
    return expandedList


def lengthenWord(word):
    return word[0:-2] + (word[-2] * randint(1, 5)) + word[-1] # multiply second last letter by 1-5


tweet()
