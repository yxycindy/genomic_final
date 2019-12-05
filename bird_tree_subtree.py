# for reading, writing, and analyzing files--like .nex--related to phylogenic trees
import dendropy

def view_phylogenic_tree():
    print(tree2.as_ascii_plot())


if __name__ == '__main__':
    FILEPATH = "C:\\Users\\Shuha\\Downloads\\tree-pruner-7bb9002c-63e8-4a5d-b6ee-139ae5e0f95d\\output.nex"
    tree2 = dendropy.Tree.get(file=open(FILEPATH, "r"), schema="nexus")
    view_phylogenic_tree()

# def parse_bird_tree_download(filepath):
#     # Strings that mark the end and beginning of .NEX output file from BirdTree.org
#     BEGIN = "BEGIN TREES;\n"
#     END = "END;\n"
#     with open(filepath, 'r') as f:  # open the file
#         output_list = f.readlines()
#         start = output_list.index(BEGIN)
#         end = output_list.index(END)
#         if end == -1 or start == -1 or end <= start:
#             raise Exception("No tree exists or file is not in right format.")
#         subtree = output_list[start+1:end]
#         for a in subtree:
#             print(a.strip())