#!/usr/bin/python3

from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import os

directory = '/home/aryeh/pdb/unzipped'

# parse structure, insert required pdb file here
p = PDBParser()
for filename in os.listdir(directory):
	try:
		structure = p.get_structure("file", filename) 	
    	# use only the first model
		model = structure[0]
    	# calculate DSSP
		dssp = DSSP(model, filename, file_type='PDB')
	except Exception:
		pass
    	# extract all DSSP information
		for z in range(len(dssp)):
			a_key = list(dssp.keys())[z]
			print(dssp[a_key])


# This BioPython script I wrote extracts solvent accessibility readings from PDB files. On a set of 200,000 PDB files it takes 2 weeks to complete. Will further optimise the program for future use.

# Sample output:

#(1, 'A', '-', 1.0, -105.5, -32.5, 0, 0.0, 4, -1.9, 0, 0.0, 5, -0.1)
#(2, 'E', 'H', 0.5257731958762887, -68.2, -41.3, 2, -0.2, 4, -1.5, 1, -0.2, 5, -0.1)
#(3, 'I', 'H', 0.2781065088757396, -68.0, -38.1, 2, -0.2, 4, -2.0, 1, -0.2, -1, -0.2)
#(4, 'A', 'H', 0.4811320754716981, -66.7, -37.3, 1, -0.2, 4, -2.2, 2, -0.2, -2, -0.2)
#(5, 'A', 'H', 0.5283018867924528, -64.5, -38.1, -4, -1.9, 4, -1.9, 1, -0.2, -1, -0.2)
#(6, 'I', 'H', 0.047337278106508875, -69.3, -39.1, -4, -1.5, 4, -2.5, 2, -0.2, -2, -0.2)
#(7, 'E', 'H', 0.3556701030927835, -61.9, -41.0, -4, -2.0, 4, -1.7, 1, -0.2, -2, -0.2)
#(8, 'Y', 'H', 0.8603603603603603, -63.2, -41.1, -4, -2.2, 4, -1.5, 1, -0.2, -1, -0.2)
#(9, 'E', 'H', 0.29896907216494845, -68.2, -38.0, -4, -1.9, 4, -2.1, 1, -0.2, -1, -0.2)
#(10, 'Q', 'H', 0.08585858585858586, -64.9, -33.4, -4, -2.5, 4, -2.5, 1, -0.2, -1, -0.2)
#...
