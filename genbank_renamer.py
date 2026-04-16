#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to rename fasta sequences, only the species names plus
the accession is retained.
Script will look for all files ending in a pattern and will keep
the species names plus the accesion number
"""

import glob
from Bio import SeqIO

files = glob.glob('*.fasta')
#print(files) 

for file in files:
	# let's create a filename name first
	print("working on",file)
	f_root = file.split('.fasta')[0]
	print(f_root)
	new_file = f_root + '.rn.fas'
	print(new_file)


	#parsing the sequences names
	records = list(SeqIO.parse(file, "fasta"))
	for record in records:
		seq_name = str(record.name)
		seq_desc = str(record.description)
		#print(seq_name)
		#print(seq_desc)
		name_elements = seq_desc.split(' ')
		#print(name_elements)
		genus = name_elements[1]
		species = name_elements[2]
		accession = seq_name.split('.')[0]
		#print(genus,species,accession)
		new_name = genus + '_' + species + '_' + accession
		print(new_name)
		record.id = new_name
		record.name = ""
		record.description = ""

	outfile = new_file
	SeqIO.write(records, outfile, 'fasta')
