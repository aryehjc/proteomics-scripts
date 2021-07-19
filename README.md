# aryeh
Creating scripts to optimize proteomics workflows.

Antibody CDR Finders: Finds Light Chain and Heavy Chain sequences according to Kabat and Chothia rules for antibody sequence numbering.
Please note that Light Chain CDR3 finder and Heavy Chain CDR3 finder are both only 99% accurate, I have included a method for 100% accuracy within the lightchainCDR3finder script and heavychainCDR3finder1 script, making use of grep and GNU Parallel to amend the inaccurate sequence strings.


phobiusscript: Runs Phobius program 20 times in parallel to produce text file that can be converted to Excel format. Phobius outputs text file with headers giving number and location of membrane proteins in bacterial genome FASTA data as well as any signal peptides present.

MaxQuantbash: restarts MaxQuant proteomics program immediately after crashing. 

MassRecalibration, CalculatePeakProperties and TestRawFiles - starts MaxQuant from specific point after crashing. Exploits 'partial-processing' feature in MaxQuant command line, i.e. 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=5 for Testing Raw Files step, 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=10 for Calculating Peak Properties step, 
mono MaxQuant/bin/MaxQuantCmd.exe mqpar.xml --partial-processing=14 for Mass Recalibration step.


R barplot example: Produces a bar graph in R.
