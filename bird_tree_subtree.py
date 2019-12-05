# for reading, writing, and analyzing files--like .nex--related to phylogenic trees
from dendropy import Tree, TreeList

#################################################################################################################
'''
BRIEF BREAKDOWN OF DENDROPY TO GET YOU STARTED:

Our bird phylogenetic tree data has >= 100 trees in the output.nex file. The TreeList class is used to handle
a list of phylogenetic trees (like in our case) while Tree is used to handle one phylogenetic tree.
Dendropy accepts .nex (nexus) files among many others.

install dendropy at https://dendropy.org/downloading.html
'''
#################################################################################################################
'''
Helpful methods for the TREE class from the link https://dendropy.org/library/treemodel.html#dendropy.datamodel.treemodel.Tree
tree.as_ascii_plot()
    print tree out in ascii
tree.ageorder_node_iter(descending=True)
    iterate through node of the tree from root down
tree.edges()
    returns list of edges of tree.
'''
#################################################################################################################

if __name__ == '__main__':
    FILEPATH = 'C:\\Users\\Shuha\\PycharmProjects\\Computational_Genomics\\genomic_final\\bird_phylogenic_tree.nex'
    treelist = TreeList.get(path=FILEPATH, schema="nexus")
    assert len(treelist) == 200
    print(treelist[0].as_ascii_plot())