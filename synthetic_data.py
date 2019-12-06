import random
from random import seed
from random import randint
import networkx as nx
import matplotlib.pyplot as plt



# cparent = "GTTGATAAGCAAGCATCTCATTTTGTGCATATACCTGGTCTTTCGTATTCTGGCGTGAAGTCGCCGNCTGAATGCCAGCAATCTCTTTTTGAGTCTCATT"
# cparent = "GTTGATAAGCAAGCA"
# cparent = "ATGC"

# depth = 5
# seed(5)
G = nx.DiGraph()

def generate_genome():
# mutate the parent genome for every child 
# output a list of genome
	# cparent = "GTTGAT"
	cparent = "ATGC"
	depth = 2
	seed(5)
	genome_list = []
	child_list = []
	cur_list = [cparent]
	genome_list.append(cparent)

	for i in range(depth):
		child_list, cur_list = cur_list, []
		# print("*************")
		for item in child_list:
			# print("-------------")
			# generate child for every genome
			for j in range(randint(2, 8)):
				pos_to_change = randint(0, len(item)-1)
				new_child = mutate(pos_to_change, item)
				# print(new_child)
				# append new chile to list and trees
				genome_list.append(new_child)
				cur_list.append(new_child)

				#add item->child edge
				G.add_edges_from([(item, new_child)])

	return genome_list

def mutate(pos, item):
	base = ['A', 'T', 'G', 'C']
	# seed(5)
	num = randint(0, 2)
	if num == 0:
		#insert
		return (item[:pos] + random.choice(base) + item[pos:])
	elif num == 1:
		#delete
		return (item[:pos] + item[pos+1:])
	else:
		#mismatch
		b = random.choice(base)
		while(b == item[pos]):
			b = random.choice(base)
		return (item[:pos] + b + item[pos+1:])


def generate_graph():
	return


generate_genome()
# print(genome_list)
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='b', arrows=True)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
plt.show()