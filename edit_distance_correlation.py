# TODO: measure correlations between minhash, weighted jaccard, and OMH with true edit distance

# Make some graphs
from random import choice
from string import ascii_uppercase

def gen_string_universe():
    length_range = 12
    s = sum(([''.join(choice(ascii_uppercase) for _ in range(l))] for l in range(1, length_range)))
    # print(''.join(choice(ascii_uppercase) for _ in range(12)))

gen_string_universe()