import timeit
import collections
from compute_mst import *
from minhash import *
from synthetic_data import *
from create_tree import visualize_graph
import matplotlib.pyplot as plt

# get the synthetic data 
# syn_genome = generate_genome()
KMER_LENGTH=5
SKETCH_SIZE=10
DEPTH=6


def edit_distance_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			edges[edit_distance(syn_genome[i], syn_genome[j])].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)


def get_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	sketches = [minhash(string_to_kmers(i, KMER_LENGTH), SKETCH_SIZE) for i in syn_genome]
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-jaccard_hash(sketches[i], sketches[j])
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)


def get_weighted_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	sketches = [weighted_minhash(string_to_kmers(i, KMER_LENGTH), SKETCH_SIZE) for i in syn_genome]
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-weighted_jaccard_hash(sketches[i], sketches[j])
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)

def get_order_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	sketches = [order_minhash(string_to_kmers(i, KMER_LENGTH), SKETCH_SIZE) for i in syn_genome]
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-hamming_similarity(sketches[i], sketches[j])
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)
	# return hamming_similarity(order_minhash(string_to_kmers(g1, KMER_LENGTH), SKETCH_SIZE), order_minhash(string_to_kmers(g2, KMER_LENGTH), SKETCH_SIZE)

edit_dis_list = []
minhash_list = []
weighted_minhash_list = []
order_minhash_list = []
d = []

for depth in range(2, DEPTH):
    syn_genome = generate_genome(depth)
    d.append(len(syn_genome))
    start = timeit.default_timer()
    edit_distance_G()
    stop = timeit.default_timer()
    edit_dis_list.append(stop - start)
    print('Time for edit distance: ', stop - start) 


    start = timeit.default_timer()
    get_minhash_G()
    stop = timeit.default_timer()
    minhash_list.append(stop - start)
    print('Time for minhash: ', stop - start) 

    start = timeit.default_timer()
    get_weighted_minhash_G()
    stop = timeit.default_timer()
    weighted_minhash_list.append(stop - start)
    print('Time for weighted_minhash: ', stop - start) 

    start = timeit.default_timer()
    get_order_minhash_G()
    stop = timeit.default_timer()
    order_minhash_list.append(stop - start)
    print('Time for order_minhash: ', stop - start) 


plt.plot(d, edit_dis_list, label='edit dis')
plt.plot(d, minhash_list, label='minhash')
plt.plot(d, weighted_minhash_list, label='weighted minhash')
plt.plot(d, order_minhash_list, label='ordered minhash')
plt.xlabel('Depth of the synthetic tree')
plt.ylabel('time in seconds to generate tree')
plt.legend()
# plt.savefig('test^^^^^.png') 
plt.show()