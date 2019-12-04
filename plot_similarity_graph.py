
def get_edit_distance_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return edit_similarity(g1, g2)


def get_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return jaccard_hash(minhash(string_to_kmers(g1, 2), 3), minhash(string_to_kmers(g2, 2), 3))


def get_weighted_minhash_res(g1, g2):
	'''get the edit distance for every genome parit in synthetic data'''
	return weighted_jaccard_hash(weighted_minhash(string_to_kmers(g1, 2), 3), weighted_minhash(string_to_kmers(g2, 2), 3))




m = minhash(stream, h)
minhash.jaccard_hash(m1, m2)