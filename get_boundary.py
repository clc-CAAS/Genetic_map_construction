#!/usr/bin/python
import os
import argparse
import re

parser=argparse.ArgumentParser(description='')
parser.add_argument('-i', type =argparse.FileType('r'),help='')
#parser.add_argument('-o', type =argparse.FileType('w'),help='')
parser.add_argument('-chro', type = str ,help='chromsome')
args=parser.parse_args()
debug=True

#eg:python get_boundary.py -i snp_idea_samples_genotype_BC4_1S1_for_show5.txt -chro A03

o1 = open(args.chro + '_heterozygous_genotype.txt','w')
o2 = open(args.chro + '_donor_parent_genotype.txt','w')

newline = ''
for line in args.i:
	list1 = line.strip().split('\t')
	if list1[0] == '#CHROM':
		o1.write(line)
		o2.write(line)
	else:
		offspring = list1[4]
		Chiifu_2 = list1[5]
		R_o_18 = list1[6]
		if list1[0] == args.chro and offspring == Chiifu_2[0]+ R_o_18[0]:
			o1.write(line)
		elif list1[0] == args.chro and offspring == R_o_18:
			o2.write(line)

args.i.close()
o1.close()
o2.close()
