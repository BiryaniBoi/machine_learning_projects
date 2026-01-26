import string
from util import *

def word_ladder_neighbors(current_word, valid_words):
    '''
    Given a word (current_word) as a string and a set of valid words,
    returns a list of words that are all one letter different 
    than current_word.
    '''
    alphabet = string.ascii_lowercase
    neighbors = []
    for i in range(len(current_word)):
        for letter in alphabet:
            next_word = current_word[:i] + letter + current_word[i+1:]
            if next_word in valid_words:
                neighbors.append(next_word)
    return neighbors

def word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word.
    '''
    queue = [[start_word]]
    visited = set()
    while len(queue) > 0:
        partial_path = queue.pop(0)
        if partial_path[-1] == end_word:
            return partial_path
        last_word = partial_path[-1]
        if last_word not in visited:
            visited.add(last_word)
            for next_word in word_ladder_neighbors(last_word, valid_words):
                queue.append(partial_path + [next_word])

    return None

def better_word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word. This search should use heuristic_function to speed up
    the search.
    '''
    queue = PriorityQueue()
    queue.update([start_word], 0)
    visited = set()
    while queue:
        partial_path = queue.pop()
        if partial_path[-1] == end_word:
            return partial_path
        last_word = partial_path[-1]
        if last_word not in visited:
            visited.add(last_word)
            for next_word in word_ladder_neighbors(last_word, valid_words):
                queue.update(partial_path + [next_word], heuristic_function(next_word, end_word))

    return None

def heuristic_function(state, end_word):
    return len([state[x] for x in range(len(state)) if state[x] != end_word[x]])


if __name__=="__main__":
    # valid_words is a set containing all strings that should be considered valid
    # words (all in lower-case)
    with open('words_alpha.txt') as f:
        valid_words = {i.strip() for i in f}

    print("You have", len(valid_words), "words to work with.")

    start = "marcin"
    end = "weiner"

    path = better_word_ladder_search(valid_words, start, end)
    print(path)
    