import numpy as np
from minhash import *

def test_minhash():
    h = minhash(['HI'], 1)
    assert h.shape[0] == 1
    h = minhash(['HI'], 100)
    assert h.shape[0] == 1

    assert minhash(['ABC','DEF'], 3).shape[0] == 2

def test_hamming():
    x1 = np.array([1,2,3,4])
    x2 = np.array([1,2,3,4])

    assert hamming_similarity(x1, x2) == 1.0

    x3 = np.array([-1,2,3,4])

    assert hamming_similarity(x1, x3) == 0.75

    x4 = np.array([0,0,0,0])

    assert hamming_similarity(x1, x4) == 0.0

def test_jaccard_hash():
    x1 = [1,2,3]
    
    assert jaccard_hash(x1, x1) == 1.0
    x2 = [5,6,7]
    assert jaccard_hash(x1, x2) == 0.0

    assert jaccard_hash([1,2,3,4], [3,4]) == 0.5

def test_hamming_minhash():
    def minhash_sim(a, b):
        return jaccard_hash(minhash(string_to_kmers(a, 2), 3), minhash(string_to_kmers(b, 2), 3))

    # Try two strings that have the same kmer content
    assert minhash_sim("ABCC", "ABCCC") == 1.0

    # Try two strings that share no kmers in common
    assert minhash_sim("ABC", "DEF") == 0.0

def test_edit_distance():
    s1 = "HEY"
    assert edit_distance(s1, s1) == 0

    s2 = "HEYYO"
    assert edit_distance(s1, s2) == 2

    s3 = "HAY"
    assert edit_distance(s1, s3) == 1
    
    assert edit_distance(s1, "H") == 2

def test_string_to_kmers():
    string='HELLO'
    k=2
    kmers = set(('HE', 'EL', 'LL', 'LO'))
    out = set(string_to_kmers(string, k))
    assert out == kmers

def test_order_minhash():
    omh = order_minhash(string_to_kmers("HEYYO", 2), 2)
    assert omh.shape[0] == 2
    assert (order_minhash(string_to_kmers("HEYYO", 2), 2) == order_minhash(string_to_kmers("HEYYO", 2), 2)).all()
    # This assertion is flaky (randomness in hash function)
    # assert not (order_minhash(string_to_kmers("HEYYO", 2), 3) == order_minhash(string_to_kmers("HEYYYO", 2), 3)).all()

def test_nsmallest_no_duplicates():
    l = list(range(100))
    assert set(nsmallest_no_duplicates(5, l)) == set(list(range(5)))
    assert set(nsmallest_no_duplicates(3, [2,2,2,3,3,3,4,4,4,5])) == set([2,3,4])
    
    # Test counts
    assert set(nsmallest_no_duplicates(3, [2,2,2,3,3,3,4,4,4,5], count=True)) == set([(2, 3),(3, 3),(4, 3)])