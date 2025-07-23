import re

genome = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
noncoding_file = open('noncoding_genes.fa', 'w')

# dictionary to store gene name and gene information with noncoding sequences
gene_dic = {}

#  create continuous DNA sequence for the gene
for line in genome:
    if re.search(r'>', line):
        gene_name = ''
        if not re.search(r'protein_coding', line):
            # search for the gene name
            gene_name = re.findall('gene:' + '.+?\s', line)[0]
            gene_sequence = ''
    # create continuous gene sequence
    if re.search(r'^[a-zA-Z]', line):
        if gene_name != '':
            gene_sequence += line.rstrip()
            gene_dic[gene_name] = gene_sequence 
    
for keys in gene_dic:
    new_keys = re.sub('gene:', '>', keys)
    new_keys = re.sub(' ', '\n', new_keys)        
    noncoding_file.write(new_keys)
    noncoding_file.write(str(gene_dic[keys]) + '\n')

genome.close()
noncoding_file.close()
#print(gene_dic)