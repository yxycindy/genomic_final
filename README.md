# Faster Phylogenomics with Sketching
Christian Cosgrove, Xingyi Yang, Jenna Ballard, Shuhao Lai\
Computational Genomics Fall 2019

# Directions for Running Code

## To compute sketches for Avianbase bird genomes
Run `get\_sketch.py` with the following arguments:
    `-f` filename with URLs to the Avianbase genomes
    `-o` output directory for sketches
    `-a` algorithm (minhash, weighted_minhash, order_minhash)
    `-s` start index in bird genome file for which to compute sketch
       (this is in case you want to get the sketches for a specific subset of the bird genomes)
    `-e` end index in bird genome file for which to compute sketch
       (to get sketches for subset of bird genomes ending at end index, inclusive)

Sample: For running minhash on the first bird genome (to compute sketches for all 42 genomes, exclude the -s and -e flags):

`PYTHONHASHSEED=0 python3 get\_sketch.py -f avian\_genome\_links.txt -o sketches/minhash/ -a minhash -s 0 -e 0`

It takes about 23-25 minutes to compute a sketch for a single bird genome. We also provided the sketches that we have computed so that you can run the rest of the code and reproduce our results.

## To compute minimum spanning tree from sketches and  .dot file
Once sketches have been created, to compute the minimum spanning tree and .dot file,
run `create\_tree.py` with the following arguments:
    `-f` directory containing the sketches
    `-o` output directory for the .dot file
    `-a` algorithm (minhash, weighted_minhash, order_minhash)

Sample: For creating a tree from the weighted\_minhash sketches:

`python3 create\_tree.py -f sketches/weighted\_minhash/marcc\_sketches/ -o trees/ -a weighted\_minhash`

## To run unit tests
`pytest`

# link to google drive 
https://drive.google.com/drive/folders/1CdZuMulag5o9lIDH0NRrwnyY6y62\_LUJ?usp=sharing


# TODO 

3. Compute trees for Order MinHash and Weighted MinHash on Avianbase and synthetic data.

4. Compare Avianbase trees with BirdTree.org

5. Write better readme. In particular, instructions about how to run code (+ unit tests).
 Use conda environment to install pip/conda dependencies easily!

6. Write paper!
