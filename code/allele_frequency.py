#import libraries
import pandas as pd

#load data
headers = ['rsid', 'chromosome', 'position', 'genotype']
data = pd.read_csv('file name', sep='\t', comment='#', names=headers) #include genome text file from 23andMe raw data download where it says 'fil name'

# filter out missing data 
data = data[data['genotype'] != '--']

# function to calculate allel frequencies
def calculate_allele_frequencies(genotype_series):
    allele_counts = defaultdict(int)
    total_alleles = 0

    for genotype in genotype_series:
        for allele in genotype:
            allele_counts[allele] += 1
            total_alleles += 1

    allele_frequencies = {allele: count / total_alleles for allele, count in allele_counts.items()}
    return allele_frequencies

# call function and print allel frequencies
allele_frequencies = calculate_allele_frequencies(data['genotype'])
print("your Allele Frequencies:", allele_frequencies)

