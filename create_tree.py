# Script to read in sketches, compute estimate of edit distance,
# and create minimum spanning tree

import numpy as np
import minhash
import compute_mst

''' Creates map of edges to be input to kruskal
    Parameters:
      birdnames - filename containing the names of the birds, also
          corresponding to the sketch file names and bird ids

    Returns:
      edges - multimap to be read into kruskal to create minimum spanning tree
          {edit_distance : [(seq1, seq2)]}
'''
def create_edges(birdnamefile, start_idx=0, num_birds=44):
    # reading in birdname file
    birdnames = open(birdnamefile, 'r')
    namestr = birdnames.read()
    namelist = namestr.split('\n')
    namelist.remove('')
    birdnames.close()

    edges = {}

    for i in range(start_idx, num_birds):
        for j in range(i+1, num_birds):
            # Loading signature files
            f1 = 'sketches/minhash/' + namelist[i] + '.npy'
            f2 = 'sketches/minhash/' + namelist[j] + '.npy'
            sketch1 = np.load(f1)
            sketch2 = np.load(f2)

            # since we are computing minimum spanning tree, need
            # dissimilarity, not similarity
            jaccard_dist = 1-minhash.jaccard_hash(sketch1, sketch2)
            if jaccard_dist not in edges.keys():
                edges[jaccard_dist] = [(namelist[i], namelist[j])]
            else:
                edges[jaccard_dist].append((namelist[i], namelist[j]))

#            print(jaccard)
#            print(namelist[i] + ' ' + namelist[j])

    return edges

def main():

    edges = create_edges('bird_names.txt', start_idx=0, num_birds=14)
#    print(edges)
    mst = compute_mst.kruskal(edges)
    print(mst)


if __name__ == "__main__":
    main()
