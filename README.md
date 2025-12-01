# Phylogenetic Tree Comparison Project: 16S rRNA vs. TimeTree Data
This repository contains the scripts and results for a comparative bioinformatics analysis, focusing on the phylogenetic relationships of 10 diverse bacterial species. The project aims to compare a Maximum Likelihood (ML) phylogenetic tree built from 16S ribosomal RNA (rRNA) sequences with a TimeTree based on estimated species divergence times.

# Step-by-step analysis
Follow these steps in order to reproduce the phylogenetic comparison:

## Step 1: Species selection and TimeTree data acquisition

We selected 10 bacteria species. Crucially, we ensured that the chosen taxa have sufficient genetic distance for meaningful speciation time estimation. For comparison with our generated phylogenic tree, we downloaded Newick tree for the same 10 species from:

    https://timetree.org

## Step 2: 16S rRNA sequence retrieval

The fetch_16S_bacteria.py script enables fetching 10 sequences NCBI database.

    python3 fetch_16S_bacteria.py 
    
    
## Step 3: Multiple Sequence Alignment (MSA)

The gen_lab4_aligment.py script performs the alignment, which is critical for accurate phylogenetic reconstruction.

    python3 gen_lab4_aligment.py
    
## Step 4: Maximum Likelihood tree building

The iqtree2.sh bash script enables building a tree for 16S rRNA sequences.

    bash iqtree2.sh
    
## Step 5: Trees visualization and comparison

The trees_visualization.rmd script for R enables visualization of both trees and computes the Robinson-Fould metric to quantify topological differences.


# Instalation 
To successfully run the analysis scripts, the following software and libraries must be installed and accessible from your system's PATH.

## Bioinformatics Software Tools (CLT)

These external command-line tools are required for alignment and tree building:

    MAFFT: Required for Multiple Sequence Alignment (MSA) (Step 3).
    IQ-TREE2: Essential for Maximum Likelihood (ML) tree inference (Step 4).

Programming Environments & Libraries:

    
    Python 3: Required for .py scripts.
    Biopython: Necessary Python library for handling sequence and tree files.
    R and RStudio: Required for running the analysis and visualization script (trees_visualization.rmd).

Installation:

    pip install biopython

## Repository installation


git clone https://github.com/barbarapawlowskaa/gene_trees
cd gene_trees

