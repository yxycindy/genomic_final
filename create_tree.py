# Script to read in sketches, compute estimate of edit distance,
# and create minimum spanning tree

import numpy as np
import minhash
import compute_mst
from tqdm import tqdm
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Compute MST and .dot file for visualization for given bird genomes.')

    parser.add_argument("-f", dest="sketch_dir", help="set directory containing sketches", required=True)

    parser.add_argument("-o", dest="out_dir", help="set the output directory for the .dot file.", required=True)

    parser.add_argument("-a", dest="algo", help="set the desired algorithm: 'minhash', 'weighted_minhash', 'order_minhash'", required=True)

    args = parser.parse_args()

    return args

''' Creates map of edges to be input to kruskal
    Parameters:
      birdnames - filename containing the names of the birds, also
          corresponding to the sketch file names and bird ids

    Returns:
      edges - multimap to be read into kruskal to create minimum spanning tree
          {edit_distance : [(seq1, seq2)]}
'''
def create_edges(birdnamefile, sketch_dir, algo, start_idx=0, num_birds=42):
    # reading in birdname file
    birdnames = open(birdnamefile, 'r')
    namestr = birdnames.read()
    namelist = namestr.split('\n')
    namelist.remove('')
    birdnames.close()

    edges = {}

#    with tqdm(total=num_birds*(num_birds-1)/2) as pbar:
    for i in range(start_idx, num_birds):
        for j in range(i+1, num_birds):
            # Loading signature files
#            filedir = 'sketches/minhash/marcc_sketches/'
            filedir = sketch_dir
            f1 = filedir + namelist[i] + '.npy'
            f2 = filedir + namelist[j] + '.npy'
            sketch1 = np.load(f1)
            sketch2 = np.load(f2)

            if algo == 'minhash':
                # since we are computing minimum spanning tree, need
                # dissimilarity, not similarity
                jaccard_dist = 1-minhash.jaccard_hash(sketch1, sketch2)
                if jaccard_dist not in edges.keys():
                    edges[jaccard_dist] = [(namelist[i], namelist[j])]
                else:
                    edges[jaccard_dist].append((namelist[i], namelist[j]))
            elif algo == 'weighted_minhash':
                jaccard_dist = 1-minhash.weighted_jaccard_hash(sketch1, sketch2)
                if jaccard_dist not in edges.keys():
                    edges[jaccard_dist] = [(namelist[i], namelist[j])]
                else:
                    edges[jaccard_dist].append((namelist[i], namelist[j]))
            elif algo == 'order_minhash':
                edit_dist = 1-minhash.hamming_similarity(sketch1, sketch2)
                if edit_dist not in edges.keys():
                    edges[edit_dist] = [(namelist[i], namelist[j])]
                else:
                    edges[edit_dist].append((namelist[i], namelist[j]))
#                pbar.update(1)

#            print(jaccard)
#            print(namelist[i] + ' ' + namelist[j])

    return edges

def visualize_graph(mst):
    visited = {}
    outstr = "strict graph {\n"
    for k in mst.keys():
        outstr += "  \"" + k + "\";\n"
    for k in mst.keys():
        v1 = k
        for k1 in mst[k].keys():
            v2 = k1
            if v1 not in visited.keys():
                visited[v1] = []
            visited[v1].append(v2)
            e = mst[k][v2]
            if v2 not in visited.keys() or v1 not in visited[v2]: 
                outstr += "  \"" + v1 + "\" -- \"" + v2 + "\" [label=\"" + str(e) + "\"];\n"
    outstr += "}"

    return outstr

def create_dot(sketchdir, outdir, algorithm):
    edges = create_edges('bird_names.txt', sketch_dir=sketchdir, algo=algorithm, start_idx=0)
#    print(edges)
    mst = compute_mst.kruskal(edges)
#    print(mst)

    outstr = visualize_graph(mst)
    outfile = open(outdir + algorithm + '_bird_mst.dot', 'w')
    outfile.write(outstr)
    outfile.close()

def main():

    args = get_args()
    sketchdir = args.sketch_dir
    outdir = args.out_dir
    algo = args.algo

    # Params for creating graph for minhash
    sketchdir = 'sketches/order_minhash/marcc_sketches/'
    algorithm = 'order_minhash'
    create_dot(sketchdir, outdir, algorithm)


if __name__ == "__main__":
    main()
