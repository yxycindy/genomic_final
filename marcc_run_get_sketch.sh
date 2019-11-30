#!/bin/bash

#SBATCH --job-name='get_sketch'
#SBATCH --time=72:0:0
#SBATCH --nodes=1
#SBATCH --partition=shared

module load python/3.6-anaconda

PYTHONHASHSEED=0 python3 get_sketch.py -f avian_genome_links.txt -o sketches/weighted_minhash/marcc_sketches/ -a weighted_minhash
