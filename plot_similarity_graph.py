from minhash import *
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from random import choice
from string import ascii_uppercase
from tqdm import tqdm

KMER_LENGTH=2
SKETCH_SIZE=10

def gen_string_universe(length_smallest, length_largest, n):
    s = [[[''.join(choice(['A', 'C', 'T', 'G']) for _ in range(l))] for _ in range(n)] for l in range(length_smallest, length_largest + 1)]
    s = [inner for outer in s for inner in outer]
    s = [inner for outer in s for inner in outer]
    return s

def get_edit_distance_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return edit_similarity(g1, g2)


def get_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return jaccard_hash(minhash(string_to_kmers(g1, KMER_LENGTH), SKETCH_SIZE), minhash(string_to_kmers(g2, KMER_LENGTH), SKETCH_SIZE))

def get_weighted_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return weighted_jaccard_hash(weighted_minhash(string_to_kmers(g1, KMER_LENGTH), SKETCH_SIZE), weighted_minhash(string_to_kmers(g2, KMER_LENGTH), SKETCH_SIZE))

def get_order_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return hamming_similarity(order_minhash(string_to_kmers(g1, KMER_LENGTH), SKETCH_SIZE), order_minhash(string_to_kmers(g2, KMER_LENGTH), SKETCH_SIZE))

N = 100
genome = gen_string_universe(5, 10, 5)

edit_dis_list = []
minhash_list = []
weighted_minhash_list = []
order_minhash_list = []

for _ in tqdm(range(5*N)):
	g1 = choice(genome)
	g2 = choice(genome)
	edit_dis_list.append(get_edit_distance_res(g1, g2))
	minhash_list.append(get_minhash_res(g1, g2))
	weighted_minhash_list.append(get_weighted_minhash_res(g1, g2))
	order_minhash_list.append(get_order_minhash_res(g1, g2))


plt.scatter(edit_dis_list, minhash_list, s=1)
plt.scatter(edit_dis_list, weighted_minhash_list, s=1)
plt.scatter(edit_dis_list, order_minhash_list, s=1)
plt.title('Comparison of similarity estimators with true edit similarity')
plt.legend(['MinHash', 'Weighted MinHash', 'Order MinHash'])
plt.ylabel('Similarity estimate')
plt.xlabel('True edit similarity')
plt.savefig('similarity_graph.png')