# Runs MinHash and OrderMinHash

from minhash import *
from io import StringIO
import time
import numpy as np
import avianbase

def main():

    link_fname = 'avian_genome_links.txt'
    start_idx = 5

    a = avianbase.Avianbase(filename=link_fname, out_dir='./tmp', start=start_idx, cache=True)

    birdnamefile = 'bird_names.txt'
    birdnames = open(birdnamefile, 'r')
    namestr = birdnames.read()
    namelist = namestr.split('\n')
    namelist.remove('')
    birdnames.close()

    idx = start_idx

    # For minhash
    for url, g in a:
        stream = avianbase.kmers_from_file(g, 3)
        m = minhash(stream, 10000)
        print(m)

        outfilename = namelist[idx]
        np.save('sketches/minhash/' + outfilename + '.npy', m)
        idx += 1

if __name__ == "__main__":
    main()
