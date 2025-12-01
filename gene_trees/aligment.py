from Bio.Align.Applications import MafftCommandline

mafft_cline = MafftCommandline(input="bacteria_16S.fasta") 
stdout, stderr = mafft_cline() 

with open("bacteria_16S_aligned.fasta", "w") as handle: 
    handle.write(stdout)