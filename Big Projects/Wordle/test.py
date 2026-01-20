import random

def WORDS(path='words.txt'):
    with open(path) as f:
        return f.read().split()

def GUESSES(path='guesses.txt'):
    with open(path) as f:
        return f.read().split()

def WORD(words):
    return random.choice(words)

def CALCULATE(user, word):
    result = [0] * 5
    duplicate = list(word)

    for i in range(5):
        if user[i] == word[i]:
            result[i] = 2
            duplicate[i] = None

    for i in range(5):
        if user[i] in duplicate and result[i] == 0:
            result[i] = 1
            duplicate[duplicate.index(user[i])] = None
    return result