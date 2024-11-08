# aryeh
Creating scripts to optimize proteomics workflows. Updated Nov 8 2024
with Extract_Accession.py, Download_Accession, used with mycobacterium_accession_numbers.txt

after that


1) cat downloaded_genomes/*.fasta > combined_genomes.fasta 
2) makeblastdb -in combined_genomes.fasta -dbtype nucl -out downloaded_genomes/db
3) blastn -query your_query.fasta -db downloaded_genomes/db -out results.txt -max_target_seqs 5 -outfmt 6
4) above for my 2 phages 


Antibody CDR Finders: Finds Light Chain and Heavy Chain sequences (in FASTA format) according to Kabat and Chothia rules for antibody sequence numbering.
Please note that Light Chain CDR3 finder and Heavy Chain CDR3 finder are both only 99% accurate, I have included a method for 100% accuracy within the lightchainCDR3finder script and heavychainCDR3finder1 script, making use of grep and GNU Parallel to amend the inaccurate sequence strings.

S1finder: Finds S1 regions between 14-685 residues as given in https://www.nature.com/articles/s41401-020-0485-4 

RBDfinder: Finds Finds RBD regions between 319-541 residues as given in https://www.nature.com/articles/s41401-020-0485-4 

Please note that within the above scripts, 'S1finders', 'LCALL' and 'HCALL' refers to the directories I am working in, please change this into the appropriate directory name you are working with antibody FASTA sequences in. E.g. Directory LCALL in the script is called by ' for file in /LCALL/* ' and directory A becomes 'for file in /A/*'

Please note that for maximum accuracy with the CDR3 finder for Heavy Chain sequences, run heavychainCDR3finder1, heavychainCDR3finder2, and heavychainCDR3finder3 in order.

phobiusscript: Runs Phobius program 20 times in parallel to produce text file that can be converted to Excel format. Phobius outputs text file with headers giving number and location of membrane proteins in bacterial genome FASTA data as well as any signal peptides present.

MaxQuantbash: restarts MaxQuant proteomics program immediately after crashing. 

MassRecalibration, CalculatePeakProperties and TestRawFiles - starts MaxQuant from specific point after crashing. Exploits 'partial-processing' feature in MaxQuant command line, i.e. 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=5 for Testing Raw Files step, 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=10 for Calculating Peak Properties step, 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=14 for Mass Recalibration step.


R barplot example: Produces a bar graph in R.



ExtractASAFromPDBs.py : Extracts Solvent Accessibility from PDB data.


GlycanMassCalculator.py : Calculates Mass of N-Glycan.

3/5/2024 - Align_Script.py, delta2fasta.py and rubyscript.rb added. Run them in that order to obtain CSVs FASTAs of alignments between 1 reference and multiple genome assemblies, to run in Locate-Insertion-Regions (written by myself)
