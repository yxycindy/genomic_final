import numpy as np
from collections import Counter
import heapq
from tqdm import tqdm

def nsmallest_no_duplicates(n, iterable, count=False, order=False):
    """ Compute the n smallest elements WITHOUT counting duplicates 
        Optional: count the number of occurrences of the n smallest elements
    """
    keys = Counter()
    heap = []
    for i, v in enumerate(iterable):
        key = -v[0] if isinstance(v, tuple) else -v
        value = v[1] if isinstance(v, tuple) else v
        if len(heap) < n:
            if key not in keys:
                heapq.heappush(heap, (key, value, i))
            keys[key] += 1
        else:
            if heap[0][0] <= key:
                if key not in keys:
                    del keys[(heap[0])]
                    heapq.heapreplace(heap, (key, value, i))
                keys[key] += 1
    if count:
        return [(val, keys[k]) for k, val, i in heap]
    elif order:
        return [((val, keys[k]), i) for k, val, i in heap]
    else:
        return [val for _, val, i in heap]

def minhash(stream, elems):
    """ Compute the minhash signature for a generator of strings """
    topk = nsmallest_no_duplicates(elems, (hash(kmer) for kmer in tqdm(stream)))
    return np.array(topk)

def weighted_minhash(stream, elems):
    """ Compute the weighted minhash signature for a generator of strings """
    topk = nsmallest_no_duplicates(elems, (hash(kmer) for kmer in tqdm(stream)), count=True)
    return np.array(topk)

def order_minhash(stream, l):
    """ Compute the order minhash signature of a stream of kmers """
    """ See https://github.com/Kingsford-Group/omhismb2019/blob/master/omh_compute/omh.hpp for more details """
    topl = nsmallest_no_duplicates(l, (hash(kmer) for kmer in tqdm(stream)), order=True)
    # Sort topl by kmer position
    return np.array([tup for tup, h in sorted(topl, key=lambda x: x[1])])

def hamming_similarity(s1, s2):
    """ Compute the hamming similarity between two signatures """
    count = 0
    for i in range(min(len(s1), len(s2))):
        if (s1[i] == s2[i]).all():
            count += 1

    return count / max(len(s1), len(s2))

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
    
def jaccard_hash(ha, hb):
    """ Compute the jaccard similarity estimate from two minhash signatures """
    ha = set(ha)
    hb = set(hb)
    X = ha.union(hb)
    k = max(len(ha), len(hb))
    X = heapq.nsmallest(k, X)
    return len(set(X).intersection(ha, hb)) / k

def weighted_jaccard_hash(ha, hb):
    """ Compute the weighted jaccard similarity between two multisets """

    ka = {k : v for k, v in ha}
    kb = {k : v for k, v in hb}

    union = set(ka.keys()).union(kb.keys())
    intersection_count = 0
    union_count = 0
    for k in union:
        if k in ka and k in kb: # In intersection
            intersection_count += min(ka[k], kb[k])
            union_count += max(ka[k], kb[k])
        else:
            if k in ka:
                union_count += ka[k]
            else:
                union_count += kb[k]
    return intersection_count / union_count
