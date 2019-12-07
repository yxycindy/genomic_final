import timeit
import collections
from compute_mst import *
from minhash import *
from synthetic_data import *
from create_tree import visualize_graph
import matplotlib.pyplot as plt

# get the synthetic data 
# syn_genome = generate_genome()
KMER_LENGTH=2
SKETCH_SIZE=10


def tree_similarity(ground_truth, t):
    """ Compute the similarity score between a ground truth tree and a given tree (where we use the output of Kruskal)"""
    gt_pairs = set(tuple(sorted((k, v))) for k, x in ground_truth.items() for v, _ in x.items())
    t_pairs = set(tuple(sorted((k, v))) for k, x in t.items() for v, _ in x.items())
    c = 0
    for edge in t_pairs:
        if edge in gt_pairs:
            c += 1
    return c / len(gt_pairs)



def edit_distance_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			edges[edit_distance(syn_genome[i], syn_genome[j])].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	return kruskal(edges)
	


def get_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-jaccard_hash(minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	return kruskal(edges)



def get_weighted_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-weighted_jaccard_hash(weighted_minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), weighted_minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	return kruskal(edges)

	
def get_order_minhash_G():
	# generate edges 
	edges = collections.defaultdict(list)
	for i in range(0, len(syn_genome)):
		for j in range(i+1, len(syn_genome)):
			dis = 1-hamming_similarity(order_minhash(string_to_kmers(syn_genome[i], KMER_LENGTH), SKETCH_SIZE), order_minhash(string_to_kmers(syn_genome[j], KMER_LENGTH), SKETCH_SIZE))
			edges[dis].append((syn_genome[i], syn_genome[j]))

	# compute MST 
	return kruskal(edges)



syn_genome = generate_genome(2)
mst_edit_dist = edit_distance_G()
outstr = visualize_graph(mst_edit_dist)
outfile = open('trees/' + '01ed' + '_mst.dot', 'w')
outfile.write(outstr)
outfile.close()
mst_minhash = get_minhash_G()
outstr = visualize_graph(mst_minhash)
outfile = open('trees/' + '02mh' + '_mst.dot', 'w')
outfile.write(outstr)
outfile.close()
mst_wmh = get_weighted_minhash_G()
outstr = visualize_graph(mst_wmh)
outfile = open('trees/' + '03wmh' + '_mst.dot', 'w')
outfile.write(outstr)
outfile.close()
mst_omh = get_order_minhash_G()
outstr = visualize_graph(mst_omh)
outfile = open('trees/' + '04omh' + '_mst.dot', 'w')
outfile.write(outstr)
outfile.close()

print("minhash", tree_similarity(mst_edit_dist, mst_minhash))
print("wmh", tree_similarity(mst_edit_dist, mst_wmh))
print("omh", tree_similarity(mst_edit_dist, mst_omh))
print("edit dis", tree_similarity(mst_edit_dist, mst_edit_dist))