import numpy as np
from collections import Counter
import heapq

def minhash(stream, elems):
    """ Compute the minhash signature for a generator of strings """
    m = np.ones(elems, dtype=np.int64) * np.iinfo(np.int64).max
    for kmer in stream:
        for i in range(elems):
            m[i] = np.min([m[i], np.int64(hash(hash(kmer)+i))])
    return m

def weighted_minhash(stream, elems):
    """ MinHash for Jaccard similarity """
    kmer_counts = Counter()
    for kmer in stream:
        kmer_counts[kmer]+=1
    m = np.ones(elems, dtype=np.int64) * np.iinfo(np.int64).max    
    for kmer in kmer_counts:
        for i in range(elems):
            m[i] = np.min([m[i], np.int64(hash(hash(kmer)+ i + kmer_counts[kmer]))])
    return m

def order_minhash(stream, l):
    """ Compute the order minhash signature of a stream of kmers """
    """ See https://github.com/Kingsford-Group/omhismb2019/blob/master/omh_compute/omh.hpp for more details """
    kmers = list(stream)
    counts = Counter()
    for kmer in kmers:
        counts[kmer]+=1
    hashes = [(hash(hash(kmer) + counts[kmer]), i) for i, kmer in enumerate(kmers)]
    heapq.heapify(hashes)
    topl = [heapq.heappop(hashes) for _ in range(l)]
    # Sort topl by kmer position
    return np.array([h for _, h in sorted(topl, key=lambda x: x[1])])

def hamming_similarity(s1, s2):
    """ Compute the hamming similarity between two signatures """
    assert s1.shape == s2.shape
    return sum(s1 == s2) / s1.shape[0]

def string_to_kmers(s, k):
    """" Get the kmer generator from a string """
    return (s[i:i+k] for i in range(len(s) - k+1))

def edit_distance(x, y):
    """ Compute the edit distance between two strings """
    dp = np.zeros(shape=(len(x) + 1, len(y) + 1), dtype=np.int)

    dp[:, 0] = np.arange(0, len(x) + 1)
    dp[0, :] = np.arange(0, len(y) + 1)

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i,j] = dp[i - 1, j - 1]
                continue

            dp[i,j] = min(1 + dp[i - 1, j - 1], dp[i - 1, j] + 1, dp[i, j - 1] + 1)

    return dp[len(x), len(y)]

def edit_similarity(x, y):
    """ Quantity in [0,1] measuring similarity between two strings """
    return 1.0 - edit_distance(x,y) / max(len(x), len(y))