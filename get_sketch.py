# Runs MinHash and OrderMinHash

from minhash import *
from io import StringIO
import time
import numpy as np
import avianbase
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Create the sketches for given bird genomes.')

    parser.add_argument("-f", dest="link_fname", help="set file with links to genome files.", required=False, default="avian_genome_links.txt")

    parser.add_argument("-o", dest="out_dir", help="set the output directory for the sketches.", required=True)

    parser.add_argument("-a", dest="algo", help="set the desired algorithm: 'minhash', 'weighted_minhash', 'order_minhash'", required=True)

    parser.add_argument("-s", dest="start_idx", help="set the start index of the bird genome to start with from the file", required=False, default=0)

    parser.add_argument("-e", dest="end_idx", help="set the end index of the bird genome to end with from the file", required=False, default=np.iinfo(np.int64).max)

    parser.add_argument("-n", dest="num_hash", help="set the number of hash functions to use", required=False, default=10000)

    parser.add_argument("-k", dest="kmer_len", help="set the kmer length", required=False, default=3)

    args = parser.parse_args()

    return args


def get_minhash_sketch(a, namelist, idx, outdir, h, k):
    # For minhash
    for url, g in a:
        stream = avianbase.kmers_from_file(g, k)
        m = minhash(stream, h)
        print(m)

        outfilename = namelist[idx]
        np.save(outdir + outfilename + '.npy', m)
        idx += 1

def get_weighted_minhash_sketch(a, namelist, idx, outdir, h, k):
    # For weighted minhash
    for url, g in a:
        stream = avianbase.kmers_from_file(g, k)
        m = weighted_minhash(stream, h)
        print(m)

        outfilename = namelist[idx]
        np.save(outdir + outfilename + '.npy', m)
        idx += 1

def get_order_minhash_sketch(a, namelist, idx, outdir, h, k):
    # For order minhash
    for url, g in a:
        stream = avianbase.kmers_from_file(g, k)
        m = order_minhash(stream, h)
        print(m)

        outfilename = namelist[idx]
        np.save(outdir + outfilename + '.npy', m)
        idx += 1

def main():

    args = get_args()
    outdir = args.out_dir
    algo = args.algo
    start_idx = args.start_idx
    end_idx = args.end_idx
    h = args.num_hash
    k = args.kmer_len


    link_fname = 'avian_genome_links.txt'

    a = avianbase.Avianbase(filename=link_fname, out_dir='./tmp', start=start_idx, end=end_idx, cache=True)

    birdnamefile = 'bird_names.txt'
    birdnames = open(birdnamefile, 'r')
    namestr = birdnames.read()
    namelist = namestr.split('\n')
    namelist.remove('')
    birdnames.close()

    idx = start_idx

    if algo == "minhash":
        get_minhash_sketch(a, namelist, idx, outdir, h, k)
    elif algo == "weighted_minhash":
        get_weighted_minhash_sketch(a, namelist, idx, outdir, h, k)
    elif algo == "order_minhash":
        get_order_minhash_sketch(a, namelist, idx, outdir, h, k)
    else:
        print("Invalid algorithm.")

if __name__ == "__main__":
    main()
