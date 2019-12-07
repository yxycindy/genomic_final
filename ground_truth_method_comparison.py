import os

import create_tree
import tree_similarity
import ground_truth_tree
import compute_mst


LIST_GROUND_TRUTH = ground_truth_tree.create_tree(num_trees=-1)
NUM = len(LIST_GROUND_TRUTH)
ALGORITHMS = ['minhash', 'order_minhash', 'weighted_minhash']


def compare_all_trees(tree):
    total = 0
    for gt_tree in LIST_GROUND_TRUTH:
        score = tree_similarity.tree_similarity(gt_tree, tree)
        total = total + score
    avg_score = total / NUM
    return avg_score


def visualize_graph(mst, outdir, marker):
    outstr = create_tree.visualize_graph(mst)
    filepath = outdir + marker + '_bird_mst'
    outfile = open(filepath + '.dot', 'w')
    outfile.write(outstr)
    outfile.close()

    # Now creating png file.
    myCmd = 'dot -Tpng ' + (filepath + '.dot') + ' > ' + filepath + '.png'
    os.system(myCmd)


def sample_few_ground_truth():
    SAMPLE = 3
    outdir = 'C:/Users/Shuha/Downloads/genomic_trees'
    tree_list = ground_truth_tree.create_tree(num_trees=SAMPLE)
    for i in range(0, len(tree_list)):
        visualize_graph(tree_list[i], outdir, str(i))


if __name__ == '__main__':
    #sample_few_ground_truth()
    '''
    Most recent results:
    ALGORITHM: minhash, AVG SCORE: 0.104193
    ALGORITHM: order_minhash, AVG SCORE: 0.073409
    ALGORITHM: weighted_minhash, AVG SCORE: 0.040909
    '''
    for algorithm in ALGORITHMS:
        sketch_dir = 'sketches/' + algorithm + '/marcc_sketches/'
        edges = create_tree.create_edges('bird_names.txt', sketch_dir=sketch_dir, algo=algorithm, start_idx=0)
        tree = compute_mst.kruskal(edges)
        score = compare_all_trees(tree)
        print('ALGORITHM: %s, AVG SCORE: %f' % (algorithm, score))
