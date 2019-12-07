# Faster Phylogenomics with Sketching
Christian Cosgrove, Xingyi Yang, Jenna Ballard, Shuhao Lai\
Computational Genomics Fall 2019

# Directions for Running Code
## Setup
- `python3 -m venv env`
- `source env/bin/activate.csh`
- `pip3 install -r requirements.txt`

## List of Files
- `minhash.py`: implementations for edit distance, minhash, weighted minhash and ordered minhash 
- `plot_similarity_graph.py`: methods to plot the performance of minhash / OMH / WMH with varying k-mer length, and sketch size
- `tree_similarity.py`: methods to calculate the similarity between different phylogenomic trees
- `compute_mst.py`: compute minimum spanning tree given a list of edges
- `create_tree.py`: Script to read in sketches, compute estimate of edit distance, and create minimum spanning tree
- `get_sketch.py`: Get sketch for minhash and ordered minhash
- `synthetic_data.py`: generate synthetic data



## To benchmark runtime for methods on synthetic data.
Run `python benchmark_runtime.py` 
- set `KMER_LENGTH` to change the kmer lenth of the input genome
- set `SKETCH_SIZE` to change the size of sketch when computing the minhash
- set `DEPTH` to change the depth of the synthetic phylogenomic tree which varies the size of input genome list

## To Compare the Performance of minhash / OMH / WMH with edit distance in terms of similarity 
Run `python3 plot_similarity_graph.py` 

## To compare accuracy of MinHash, Weighted MinHash, and Order MinHash to ground truth.
Run `python3 ground_truth_method_comparison.py`

## To compute sketches for Avianbase bird genomes
**Warning: this takes a long time (~24 hours). To reproduce the rest of the Avianbase results, skip to the next section.**
Run `get_sketch.py` with the following arguments:
- `-f` filename with URLs to the Avianbase genomes
- `-o` output directory for sketches
- `-a` algorithm (minhash, weighted\_minhash, order\_minhash)
- `-s` start index in bird genome file for which to compute sketch
       (this is in case you want to get the sketches for a specific subset of the bird genomes)
- `-e` end index in bird genome file for which to compute sketch
       (to get sketches for subset of bird genomes ending at end index, inclusive)

Sample: For running minhash on the first bird genome (to compute sketches for all 42 genomes, exclude the -s and -e flags):

`PYTHONHASHSEED=0 python3 get_sketch.py -f avian_genome_links.txt -o sketches/minhash/ -a minhash -s 0 -e 0`

It takes about 23-25 minutes to compute a sketch for a single bird genome. We also provided the sketches that we have computed so that you can run the rest of the code and reproduce our results.

## To compute minimum spanning tree from sketches and produce .dot and .png files
Once sketches have been created, to compute the minimum spanning tree and output
    .dot and .png files
run `create_tree.py` with the following arguments:
-    `-f` directory containing the sketches
-    `-o` output directory for the .dot and .png files
-    `-a` algorithm (minhash, weighted\_minhash, order\_minhash)

Sample: For creating a tree from the `weighted_minhash` sketches:

`python3 create_tree.py -f sketches/weighted_minhash/marcc_sketches/ -o trees/ -a weighted_minhash`

## To run unit tests
To ensure that our core sketching algorithms and helper functions were working properly, we wrote unit tests. To run unit tests, simply use `pytest`.

