import timeit
import collections
from compute_mst import *
from minhash import *
from synthetic_data import *
from create_tree import visualize_graph

# get the synthetic data 
syn_genome = generate_genome()
KMER_LENGTH=2
SKETCH_SIZE=10


def edit_distance_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			edges[edit_distance(syn_genome[i], syn_genome[j])].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)

	outstr = visualize_graph(mst)
	outfile = open('trees/' + 'edit_dis' + '_bird_mst.dot', 'w')
	outfile.write(outstr)
	outfile.close()



def get_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-jaccard_hash(minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)

	outstr = visualize_graph(mst)
	outfile = open('trees/' + 'minhashtest' + '_bird_mst.dot', 'w')
	outfile.write(outstr)
	outfile.close()


def get_weighted_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = weighted_jaccard_hash(weighted_minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), weighted_minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)

def get_order_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = hamming_similarity(order_minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), order_minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	mst = kruskal(edges)
	# return hamming_similarity(order_minhash(string_to_kmers(g1, KMER_LENGTH), SKETCH_SIZE), order_minhash(string_to_kmers(g2, KMER_LENGTH), SKETCH_SIZE)

start = timeit.default_timer()
edit_distance_G()
stop = timeit.default_timer()
print('Time for edit distance: ', stop - start) 


start = timeit.default_timer()
get_minhash_G()
stop = timeit.default_timer()
print('Time for minhash: ', stop - start) 

start = timeit.default_timer()
get_weighted_minhash_G()
stop = timeit.default_timer()
print('Time for weighted_minhash: ', stop - start) 

start = timeit.default_timer()
get_order_minhash_G()
stop = timeit.default_timer()
print('Time for order_minhash: ', stop - start) 



