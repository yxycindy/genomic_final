def tree_similarity(ground_truth, t):
    """ Compute the similarity score between a ground truth tree and a given tree (where we use the output of Kruskal)"""

    gt_pairs = set((k, v) for k, x in ground_truth.items() for v, _ in x.items())
    t_pairs = set((k, v) for k, x in t.items() for v, _ in x.items())
    c = 0
    for edge in t_pairs:
        if edge in gt_pairs:
            c += 1
    return c / len(gt_pairs)