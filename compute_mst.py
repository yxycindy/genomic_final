''' Computes minimum spanning tree given a list of edges
    Parameters:
       edges: map {edit_distance : [(seq1, seq2)]} where seq1 and seq2 are
              unique identifiers for each genome
       ***NOTE: mst is not unique if there are multiple sequence pairs with the
              same edit distance

    Returns:
       mst: dictionary corresponding to the minimum spanning tree for these sequences
              based on edit distance {seq1 : {seq2 : edit_distance}}

'''
def kruskal(edges):
    mst = {}
    connection_ids = {}
    setnum = 0
    for e in sorted (edges.keys()):
        for i in range(len(edges[e])):
            start = edges[e][i][0]
            end = edges[e][i][1]
            # both seqs have not been added yet
            if start not in mst.keys() and end not in mst.keys():
                mst[start] = {end : e}
                mst[end] = {start : e}
                connection_ids[start] = [setnum]
                connection_ids[end] = connection_ids[start]
                setnum += 1
            # only the second seq has not been added yet
            elif end not in mst.keys():
                mst[start][end] = e
                mst[end] = {start : e}
                connection_ids[start][0] = setnum
                connection_ids[end] = connection_ids[start]
                setnum += 1
            # only the first seq has not been added yet
            elif start not in mst.keys():
                mst[start] = {end : e}
                mst[end][start] = e
                connection_ids[end][0] = setnum
                connection_ids[start] = connection_ids[end]
                setnum += 1
            # both sequences have been added but they belong
            # to different components
            elif (connection_ids[start][0] != connection_ids[end][0]):
                mst[start][end] = e
                mst[end][start] = e
                # change all set assignments to setnum for both components
                connection_ids[start][0] = setnum
                # need to manually loop through to link all nodes in the
                # components that are being joined
                for c in connection_ids:
                    if connection_ids[c][0] == connection_ids[end][0]:
                        connection_ids[c] = connection_ids[start]
                setnum += 1

    return mst
