import random
from random import seed
from random import randint


# cparent = "GTTGATAAGCAAGCATCTCATTTTGTGCATATACCTGGTCTTTCGTATTCTGGCGTGAAGTCGCCGNCTGAATGCCAGCAATCTCTTTTTGAGTCTCATT"
# cparent = "GTTGATAAGCAAGCA"
cparent = "ATGC"
# length = len(cparent)
depth = 2
base = ['A', 'T', 'G', 'C']
genome_list = []
seed(5)

def generate_genome():
# mutate the parent genome for every child 
# output a list of genome

	child_list = []
	cur_list = [cparent]
	genome_list.append(cparent)

	for i in range(depth):
		child_list, cur_list = cur_list, []
		print("*************")
		for item in child_list:
			print("-------------")
			# generate child for every genome
			for j in range(randint(2, 8)):
				pos_to_change = randint(0, len(item)-1)
				new_child = mutate(pos_to_change, item)
				print(new_child)
				# append new chile to list and trees
				genome_list.append(new_child)
				cur_list.append(new_child)




def mutate(pos, item):
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