# Faster Phylogenomics with Sketching
Christian Cosgrove, Xingyi Yang, Jenna Ballard, Shuhao Lai\
Computational Genomics Fall 2019

# Directions for Running Code

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

## To compute minimum spanning tree from sketches and  .dot file
Once sketches have been created, to compute the minimum spanning tree and output
    .dot and .png files
run `create_tree.py` with the following arguments:
    -f directory containing the sketches
    -o output directory for the .dot and .png files
    -a algorithm (minhash, weighted_minhash, order_minhash)
Once sketches have been created, to compute the minimum spanning tree and .dot file,
run `create_tree.py` with the following arguments:
    `-f` directory containing the sketches
    `-o` output directory for the .dot file
    `-a` algorithm (minhash, weighted_minhash, order_minhash)

Sample: For creating a tree from the `weighted_minhash` sketches:

`python3 create_tree.py -f sketches/weighted_minhash/marcc_sketches/ -o trees/ -a weighted_minhash`

## To run unit tests
To ensure that our core sketching algorithms and helper functions were working properly, we wrote unit tests. To run unit tests, simply use `pytest`.

# link to google drive 
https://drive.google.com/drive/folders/1CdZuMulag5o9lIDH0NRrwnyY6y62\_LUJ?usp=sharing


# TODO 

3. Compute trees for Order MinHash and Weighted MinHash on Avianbase and synthetic data.

4. Compare Avianbase trees with BirdTree.org

5. Write better readme. In particular, instructions about how to run code (+ unit tests).
 Use conda environment to install pip/conda dependencies easily!

6. Write paper!
