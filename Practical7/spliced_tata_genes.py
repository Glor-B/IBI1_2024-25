import re
# Get the input & donor and acceptor
splice = input('Choose and enter the splice donor/acceptor combination (GTAG/GCAG/ATAC):',)
# print(type(splice))
donor = splice[0:2]
acceptor = splice[2:4]
# print(donor, acceptor)

# open file needed
genome = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
TATA_file = open('TATA_genes.fa', 'w')
splice_file = open(str(splice) + '_spliced_genes.fa', 'w')

# select genes with TATA box
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
TATA_file = open('TATA_genes.fa', 'r')

def TATA_counter(target_gene):
    c = re.findall(r'TATA[A|T]A[A|T]', target_gene)
    num = len(c)
    return(num)

#create a dictionary to store all TATA genes information
gene_dic = {}
for line in TATA_file:
    if re.search(r'>', line):
        # search for the gene name
        gene_name = line
    # create continuous gene sequence
    if re.search(r'^[a-zA-Z]', line):
        gene_dic[gene_name] = line

# find sequence with target splice
for keys in gene_dic:
    counter = 0
    if re.findall(donor + '[a-zA-Z]+'+ acceptor, gene_dic[keys]):
        # all the splice in one gene, target is a list
        target = re.findall(donor + '[a-zA-Z]+'+ acceptor, gene_dic[keys])
        # count the number of TATA box
        counter += TATA_counter(target[0])
        if counter != 0:
            new_keys = keys.rstrip() + ' TATA box number: ' + str(counter) + '\n'
            splice_file.write(new_keys)
            splice_file.write(target[0] + '\n')

TATA_file.close()
splice_file.close()