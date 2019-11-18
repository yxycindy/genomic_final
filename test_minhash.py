import numpy as np
from minhash import *

def test_minhash():
    h = minhash(('HI'), 1)
    assert h.shape[0] == 1
    h = minhash(('HI'), 100)
    assert h.shape[0] == 100

def test_hamming():
    x1 = np.array([1,2,3,4])
    x2 = np.array([1,2,3,4])

    assert hamming_similarity(x1, x2) == 1.0

    x3 = np.array([-1,2,3,4])

    assert hamming_similarity(x1, x3) == 0.75

    x4 = np.array([0,0,0,0])

    assert hamming_similarity(x1, x4) == 0.0

def test_hamming_minhash():
    def minhash_sim(a, b):
        return hamming_similarity(minhash(string_to_kmers(a, 2), 10), minhash(string_to_kmers(b, 2), 10))

    # Try two strings that have the same kmer content
    assert minhash_sim("HIHI", "HIH") == 1.0

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
    assert not (order_minhash(string_to_kmers("HEYYO", 2), 3) == order_minhash(string_to_kmers("HEYYYO", 2), 3)).all()