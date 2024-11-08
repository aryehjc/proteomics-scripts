#!/usr/bin/python3

import re
# Open your SQL file for reading
with open('Abscessus_phage_and_prophage.sql', 'r') as f:
    sql_lines = f.readlines()

# Create a list to store the accession numbers
accession_numbers = []

# Define a regex pattern to match the relevant lines (case insensitive, ignore extra whitespace)
# Updated to handle the backticks around `phage`, and look for the relevant data
pattern = re.compile(r"INSERT INTO\s+`?phage`?\s+VALUES\s*\(\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)'", re.IGNORECASE)

# Flag to indicate when we are past the table definition and into the data rows
start_processing = False

# Loop through all lines in the SQL file
for line in sql_lines:
    # Look for the first INSERT INTO phage line to start processing
    if 'INSERT INTO' in line and 'phage' in line:
        start_processing = True
    
    # Only start extracting data after finding the first INSERT INTO line
    if start_processing:
        match = pattern.search(line)
        if match:
            gene_id = match.group(2)  # Accession number is the second value
            organism_name = match.group(4).strip().lower()  # The fourth value is the species name
            if 'mycobacterium' in organism_name:  # Match Mycobacterium case-insensitively
                accession_numbers.append(gene_id)

# Write the accession numbers to a text file
with open('mycobacterium_accession_numbers.txt', 'w') as out_file:
    for acc_num in accession_numbers:
        out_file.write(acc_num + '\n')

print(f"Found {len(accession_numbers)} accession numbers for Mycobacterium. Saved to 'mycobacterium_accession_numbers.txt'.")

# This is for my abscessus phage sql file according to reviewer comments
