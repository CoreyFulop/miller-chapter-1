# infinite_monkeys.py
# Implementation of the "self check" in section 1.12 of Miller and Ranum.
# A version of the "inifinite monkey theorem".
# The text wants us to aim for "methinks it is like a weasel", this implementation is bit more flexible.

import random

def generate_string(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    characters_list = []
    length = len(string)
    for i in range(length):
        random_character = random.choice(alphabet)
        characters_list.append(random_character)
    final_string = "".join(characters_list)
    return final_string

def score_string(test_string, reference_string):
    count = 0
    for i in range(len(test_string)):
        if test_string[i] == reference_string[i]:
            count += 1
    return count

def main(n, reference):
    # input n: number of iterations to attempt
    # input reference: the target string
    best_string = ""
    best_score = 0
    best_possible_score = len(reference)
    for i in range(1, n+1):
        test_string = generate_string(reference)
        test_score = score_string(test_string, reference)
        if test_score > best_score:
            best_string = test_string
            best_score = test_score
        if i%1000 == 0:
            print(f"The best string is {best_string} with a score of {best_score}.")
            print(f"Attempts: {i}")
        if best_score == best_possible_score:
            print(f"The best string is {best_string} with a score of {best_score}.")
            print(f"Attempts: {i}")
            break
