#import libraries
import pandas as pd

#load data
headers = ['rsid', 'chromosome', 'position', 'genotype']
data = pd.read_csv('file name', sep='\t', comment='#', names=headers) #include genome text file from 23andMe raw data download where it says 'fil name'

# filter out missing data 
evan_data = evan_data[evan_data['genotype'] != '--']
raina_data = raina_data[raina_data['genotype'] != '--']

# create sports gene list 
sports_genes = ['rs1815739', 'rs8192678', 'rs1042714', 'rs12678919'] #this list includes ACTN3, PPARGC1A, VEGFa, and ADRB2

# loop through list of sports genes and print out rsid, chromosome, position, and genotype for each 
for i in sports_genes:
  genotype = evan_data[evan_data['rsid'] == i]
  print(genotype)
