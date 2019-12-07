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
calc_node_ages()
    Adds attribute called age to each node where age is the sum of edge lengths from node to the tip
'''
#################################################################################################################
'''
Helpful methods for the NODE class from the link https://dendropy.org/library/treemodel.html#dendropy.datamodel.treemodel.Node
ageorder_iter()
    Iterates through nodes of subtree
child_node_iter()
    Iterate through over all nodes that are the immediate children
distance_from_tip()
    Maximum weighted length of path of self to tip.
is_leaf()
    True if the node is a tip or leaf node. 
leaf_nodes()
    All leaf_nodes descended from this node.
'''
#################################################################################################################
'''
Putting ground truth tree in the following format:
-Let there be a map called outer map.
-Put all the bird names as keys in outer map. The value is another map called an inner map.
-Suppose bird1 is a key in outer map, then its value is an outer map where all
 its keys are the birds one edge away. The value for the inner map is then a similarity metric--this 
 is technically not necessarily as only the structure of the map is analyzed not the similarity metric
'''


SCIENTIFIC_BIRD_NAME_PATH = 'C:/Users/Shuha/PycharmProjects/Computational_Genomics/genomic_final/scientific_bird_names'
COMMON_NAME_PATH = 'C:/Users/Shuha/PycharmProjects/Computational_Genomics/genomic_final/bird_names.txt'


def scientific_to_common_name_map(key_names_path, value_names_path):
    with open(key_names_path) as f:
        key_list = f.read().splitlines()
    with open(value_names_path) as f:
        value_list = f.read().splitlines()
    name_map = dict(zip(key_list, value_list))
    return name_map


name_map = scientific_to_common_name_map(SCIENTIFIC_BIRD_NAME_PATH, COMMON_NAME_PATH)


def phylogentic_tree(tree):
    tree.print_plot()


def print_formatted_tree(outer_map):
    print('PRINTING FORMATTED TREE')
    for bird in outer_map:
        print(bird)
        inner_map = outer_map[bird]
        for connected_bird in inner_map:
            print('\t' + connected_bird)


def create_tree(filepath, NUM_TREES=1):
    treelist = TreeList.get(path=filepath, schema="nexus")
    outer_map = {}
    for i in range(0, NUM_TREES):
        tree = treelist[i]
        # Iterate from root to tips of tree not including leaves.
        iterator = tree.ageorder_node_iter(include_leaves=False, descending=True)
        for node in iterator:
            # Looping nodes in tree
            children_iter = node.child_node_iter()
            for child_node in children_iter:
                # Looping through all child of node.
                if child_node.is_leaf():
                    # Add child_node as key to outer_map but first create inner_map
                    leaf_of_node_list = node.leaf_nodes()
                    leaf_of_node_list.remove(child_node)
                    inner_map = create_inner_map(child_node, leaf_of_node_list)
                    child_name = convert_name(child_node.taxon.__str__())
                    outer_map[child_name] = inner_map
    return outer_map


def create_inner_map(key_node, value_node_list, default_value=-1):
    inner_map = {}
    for node in value_node_list:
        node_name = convert_name(node.taxon.__str__())
        inner_map[node_name] = default_value
    return inner_map


def convert_name(name):
    name = name.replace('\'', '')
    return name_map[name]


if __name__ == '__main__':
    filepath = 'C:\\Users\\Shuha\\PycharmProjects\\Computational_Genomics\\genomic_final\\bird_phylogenic_tree.nex'
    formatted_tree = create_tree(filepath=filepath)
    print_formatted_tree(formatted_tree)
