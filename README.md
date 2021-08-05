# aryeh
Creating scripts to optimize proteomics workflows.

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
