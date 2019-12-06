from minhash import *
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from random import choice
from string import ascii_uppercase
from tqdm import tqdm
import random

KMER_LENGTH=3
SKETCH_SIZE=50

BASES = ['A', 'C', 'T', 'G']
def mutate(item, bases):
    pos = random.randint(0, len(item))
    num = random.randint(0, 2)
    if num == 0:
        #insert
        return (item[:pos] + random.choice(bases) + item[pos:])
    elif num == 1:
        #delete
        return (item[:pos] + item[pos+1:])
    else:
        #mismatch
        b = random.choice(bases)
        return (item[:pos] + b + item[pos+1:])

    
def gen_string_universe(length_smallest, length_largest, n, num_dups):
    s = [[[''.join(choice(BASES) for _ in range(l))] for _ in range(n)] for l in range(length_smallest, length_largest + 1)]
    s = [inner for outer in s for inner in outer]
    s = [inner for outer in s for inner in outer]
    for i in range(num_dups):
        new = choice(s)
        s.append(mutate(new, BASES))
    return s

def get_edit_distance_res(g1, g2):
    '''get the edit distance for every genome parit in synthetic data'''
    return edit_similarity(g1, g2)


def get_minhash_res(g1, g2, sketch_size=SKETCH_SIZE, kmer_length=KMER_LENGTH):
    '''get the edit distance for every genome parit in synthetic data'''
    return jaccard_hash(minhash(string_to_kmers(g1, kmer_length), sketch_size), minhash(string_to_kmers(g2, kmer_length), sketch_size))

def get_weighted_minhash_res(g1, g2, sketch_size=SKETCH_SIZE, kmer_length=KMER_LENGTH):
    '''get the edit distance for every genome parit in synthetic data'''
    return weighted_jaccard_hash(weighted_minhash(string_to_kmers(g1, kmer_length), sketch_size), weighted_minhash(string_to_kmers(g2, kmer_length), sketch_size))

def get_order_minhash_res(g1, g2, sketch_size=SKETCH_SIZE, kmer_length=KMER_LENGTH):
    '''get the edit distance for every genome parit in synthetic data'''
    s1 = order_minhash(string_to_kmers(g1, kmer_length), sketch_size)
    s2 = order_minhash(string_to_kmers(g2, kmer_length), sketch_size)
    return hamming_similarity(s1, s2)


def gen_methods_comparison():
    N = 100
    genome = gen_string_universe(10, 20, 5, 5000)

    edit_dis_list = []
    minhash_list = []
    weighted_minhash_list = []
    order_minhash_list = []

    for _ in tqdm(range(250*N)):
        g1 = choice(genome)
        g2 = choice(genome)
        edit_dis_list.append(get_edit_distance_res(g1, g2))
        minhash_list.append(get_minhash_res(g1, g2))
        weighted_minhash_list.append(get_weighted_minhash_res(g1, g2))
        order_minhash_list.append(get_order_minhash_res(g1, g2))

    plt.scatter(edit_dis_list, minhash_list, s=0.5)
    plt.scatter(edit_dis_list, weighted_minhash_list, s=0.5)
    plt.scatter(edit_dis_list, order_minhash_list, s=0.5)
    plt.title('Comparison of similarity estimators with true edit similarity')
    plt.legend(['MinHash', 'Weighted MinHash', 'Order MinHash'])
    plt.ylabel('Similarity estimate')
    plt.xlabel('True edit similarity')
    plt.savefig('similarity_graph.png')
def gen_sketch_size_comparison():
    
    N = 20
    genome = gen_string_universe(30, 40, N, N*1000)

    sketch_size_range = [2**i for i in range(1, 7)]
    vals = [[] for _ in sketch_size_range]
    edit_dis_list = []

    for _ in tqdm(range(5000)):
        g1 = choice(genome)
        g2 = choice(genome)
        edit_dis_list.append(get_edit_distance_res(g1, g2))
        for i, sketch_size in enumerate(sketch_size_range):
            vals[i].append(get_minhash_res(g1, g2, sketch_size=sketch_size))
    for distances in vals:
        plt.scatter(edit_dis_list, distances, s=1)
    plt.title('Varying sketch size')
    plt.legend(['MinHash $m$={}'.format(k) for k in sketch_size_range])
    plt.ylabel('Similarity estimate')
    plt.xlabel('True edit similarity')
    plt.savefig('sketch_size_comparison.png') 

def gen_kmer_length_comparison():
    
    N = 20
    genome = gen_string_universe(30, 40, N, N*1000)

    sketch_size_range = [2, 3, 4, 6, 8]
    vals = [[] for _ in sketch_size_range]
    edit_dis_list = []

    for _ in tqdm(range(5000)):
        g1 = choice(genome)
        g2 = choice(genome)
        edit_dis_list.append(get_edit_distance_res(g1, g2))
        for i, sketch_size in enumerate(sketch_size_range):
            vals[i].append(get_minhash_res(g1, g2, kmer_length=sketch_size))
    for distances in vals:
        plt.scatter(edit_dis_list, distances, s=1)
    plt.title('Varying $k$-mer length')
    plt.legend(['MinHash $k$={}'.format(k) for k in sketch_size_range])
    plt.ylabel('Similarity estimate')
    plt.xlabel('True edit similarity')
    plt.savefig('kmer_length_comparison.png') 

def main():
    gen_methods_comparison()
    gen_sketch_size_comparison()
    gen_kmer_length_comparison()

if __name__=="__main__":
    main()