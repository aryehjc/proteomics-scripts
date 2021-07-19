# aryeh
Creating scripts to optimize proteomics workflows.

Antibody CDR Finders: Finds Light Chain and Heavy Chain sequences according to Kabat and Chothia rules for antibody sequence numbering.
Please note that Light Chain CDR3 finder and Heavy Chain CDR3 finder are both only 99% accurate, I have included a method for 100% accuracy within the lightchainCDR3finder script and heavychainCDR3finder1 script, making use of grep and GNU Parallel to amend the inaccurate sequence strings.
