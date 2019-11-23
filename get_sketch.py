# Runs MinHash and OrderMinHash

from minhash import *
from io import StringIO
import time

def main():

    t0 = time.time()

#    # Test input
#    seq = "ACCATAGGA"

    # Parsing input file
    filename = '../avianbase/Haliaeetus_leucocephalus.fa'
    infile = open(filename, 'r')
    sstream = StringIO()
    for line in infile:
        if line[0] == '>':
            continue
#        seqlist.append(line.rstrip())
#        seq = ''.join(seqlist)
        sstream.write(line.rstrip())

    seq = sstream.getvalue()

    t1 = time.time()

    print(t1-t0)
    # ~17.5 seconds
    sstream.close()

    stream = string_to_kmers(seq, 3);

    t2 = time.time()
    print('string_to_kmers: ' + str(t2-t1))
    # ~0 seconds

    h = minhash(stream, 5);
    print(h)

if __name__ == "__main__":
    main()
