from tree_similarity import tree_similarity

def test_tree_similarity():
    gt = {'a' : {'b' : 0.1}, 'c' : {'d' : 0.2, 'e' : 0.3}}
    t = {'a' : {'b' : 0.2}, 'c' : {'d' : 0.4, 'f' : 0.3}}
    assert abs(tree_similarity(gt, t) - 2/3) < 1e-4