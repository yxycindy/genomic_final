# Testing Kruskal's implementation

import compute_mst

def main():

    # Creating edges
    edges = {1:('a','b'), 2:('d','e'), 3:('b','e'), 4:('b','d'), 5:('b','c'), 6:('c','e')}

    mst = compute_mst.kruskal(edges)

#    print(mst)

    assert(mst['a'] == {'b': 1})
    assert(mst['b'] == {'a': 1, 'e': 3, 'c': 5})
    assert(mst['c'] == {'b': 5})
    assert(mst['d'] == {'e': 2})
    assert(mst['e'] == {'d': 2, 'b': 3})

    print('Tests passed')

if __name__ == "__main__":
    main()
