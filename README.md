# aryeh
Creating scripts to optimize proteomics workflows.

Antibody CDR Finders: Finds Light Chain and Heavy Chain sequences according to Kabat and Chothia rules for antibody sequence numbering.
Please note that Light Chain CDR3 finder and Heavy Chain CDR3 finder are both only 99% accurate, I have included a method for 100% accuracy within the lightchainCDR3finder script and heavychainCDR3finder1 script, making use of grep and GNU Parallel to amend the inaccurate sequence strings.


Phobius script: Runs Phobius program 20 times in parallel to produce text file that can be converted to Excel format. Phobius outputs text file with headers giving number and location of membrane proteins in bacterial genome FASTA data as well as any signal peptides present.
