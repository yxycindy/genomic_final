from random import seed
from random import randint


parent = "GTTGATAAGCAAGCATCTCATTTTGTGCATATACCTGGTCTTTCGTATTCTGGCGTGAAGTCGCCGNCTGAATGCCAGCAATCTCTTTTTGAGTCTCATT"
length = len(parent)
depth = 10
base = ['A', 'T', 'G', 'C']
genome_list = []

def generate_genome():
# mutate the parent genome for every child 
# output a list of genome

child_list = [parent]
cur_list = []
genome_list.insert(parent)

for i in range(depth):
	for item in child_list:
	# generate child for every genome
		for j in range(randint(2, 8)):
			pos_to_change = randint(0, length-1)
			new_child = mutate(pos, item)

			# add new chile to list and trees
			genome_list.insert(new_child)
			cur_list.insert(new_child)




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