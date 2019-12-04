from minhash import *
import matplotlib.pyplot as plt


def get_edit_distance_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return edit_similarity(g1, g2)


def get_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return jaccard_hash(minhash(string_to_kmers(g1, 2), 3), minhash(string_to_kmers(g2, 2), 3))


def get_weighted_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return weighted_jaccard_hash(weighted_minhash(string_to_kmers(g1, 2), 3), weighted_minhash(string_to_kmers(g2, 2), 3))






# get a list of synthetic genome
genome = ['ATGC', 'ATAC', 'ATGAC', 'AGTGC', 'ATGCC', 'TTGC', 'TTGC', 'ATCAC', 'ATTAC', 'ATATC', 'TATAC', 'ATTAC', 'ATTGAC', 'ACGAC', 'ATGGAC', 'ATGTAC', 'GTGC', 'AGAGC', 'AGTGG', 'GTGC', 'ATCC', 'ATCGCC', 'ATGTC', 'TGCC', 'TTC', 'CTGC', 'TTGA', 'TTGTC', 'TTTGC', 'TTG']

edit_dis_list = []
minhash_list = []
weighted_minhash_list = []

for i, g1 in enumerate(genome):
	for j in range(i+1, len(genome)):
		g2 = genome[j]
		print(get_edit_distance_res(g1, g2))
		print(get_minhash_res(g1, g2))

		# print(get_weighted_minhash_res(g1, g2))
		print('-------------------')
		edit_dis_list.append(get_edit_distance_res(g1, g2))
		minhash_list.append(get_minhash_res(g1, g2))


plt.plot(edit_dis_list)
plt.plot(minhash_list) 
plt.show()