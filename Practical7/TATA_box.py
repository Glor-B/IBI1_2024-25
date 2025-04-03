import re

genome = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
TATA_file = open('TATA_genes.fa', 'w')

# dictionary to stor gene name and gene information with TATA box
gene_dic = {}
# output = re.split(r'>', genome)
# i = 1

#  create continuous DNA sequence for the gene
for line in genome:
    if re.search(r'>', line):
        # search for the gene name
        gene_name = re.findall('gene:' + '.+?\s', line)[0]
        gene_sequence = ''
    # create continuous gene sequence
    if re.search(r'^[a-zA-Z]', line):
        gene_sequence += line.rstrip()
        gene_dic[gene_name] = gene_sequence
    # to test, so limit the for loop time    
    '''i += 1
    if i == 100000:
        break'''
    
for keys in gene_dic:
    if re.search(r'TATA[A|T]A[A|T]', gene_dic[keys]):
        new_keys = re.sub('gene:', '>', keys)
        new_keys = re.sub(' ', '\n', new_keys)
        TATA_file.write(new_keys)
        TATA_file.write(str(gene_dic[keys]) + '\n')

genome.close()
TATA_file.close()
#print(gene_dic)