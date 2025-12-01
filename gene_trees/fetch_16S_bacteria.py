from Bio import Entrez
import os

Entrez.email = "student@university.edu"

ids = {
    "PX487746.1": "Bacillus_subtilis",
    "PX487804.1": "Escherichia_coli",
    "PQ124053.1": "Corynebacterium_diphtheriae",
    "PQ497088.1": "Haemophilus_influenzae",
    "PX467062.1": "Mycobacterium_tuberculosis",
    "PQ288077.1": "Vibrio_cholerae",
    "PX474619.1": "Staphylococcus_aureus",
    "PX485076.1": "Pseudomonas_aeruginosa",
    "PX459552.1": "Streptococcus_pneumoniae",
    "PV960019.1": "Clostridioides_difficile"
}

out_dir = "16S_sequences"
os.makedirs(out_dir, exist_ok=True)

for seq_id, species in ids.items():
    try:
        handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
        fasta_seq = handle.read()
        handle.close()

        out_path = os.path.join(out_dir, f"{species}.fasta")
        with open(out_path, "w") as f:
            f.write(fasta_seq)

    except Exception as e:
        print(f"Error fetching {species} ({seq_id}): {e}")

output_file = "bacteria_16S.fasta"
with open(output_file, "w") as outfile:
    for f in os.listdir(out_dir):
        if f.endswith(".fasta"):
            with open(os.path.join(out_dir, f)) as fh:
                outfile.write(fh.read())

print(f"All sequences saved and merged into {output_file}.")
