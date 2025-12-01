# Phylogenetic Tree Comparison Project: 16S rRNA vs. TimeTree Data
This repository contains the scripts and results for a comparative bioinformatics analysis, focusing on the phylogenetic relationships of 10 diverse bacterial species. The project aims to compare a Maximum Likelihood (ML) phylogenetic tree built from 16S ribosomal RNA (rRNA) sequences with a TimeTree based on estimated species divergence times.

# Step-by-step analysis
Follow these steps in order to reproduce the phylogenetic comparison:

## Step 1: species selection and TimeTree data acquisition

We selected 10 bacteria species. Crucially, we ensured that the chosen taxa have sufficient genetic distance for meaningful speciation time estimation. For comparison with our generated phylogenic tree, we downloaded Newick tree for the same 10 species from:

    https://timetree.org

## Step 2: 16S rRNA sequence retrieval

Running the sequence fetching script:

    bash
    python3 fetch_16S_bacteria.py 
