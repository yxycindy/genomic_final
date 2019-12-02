#!/bin/bash

PYTHONHASHSEED=0 python3 get_sketch.py -f avian_genome_links.txt -o sketches/test -a minhash -s 0 -e 0
