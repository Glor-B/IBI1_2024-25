import re
# Get the input & donor and acceptor
splice = input('Choose and enter the splice donor/acceptor combination (GTAG/GCAG/ATAC):',)

TATA_file = open('TATA_genes.fa', 'r')
splice_file = open(str(splice) + '_spliced_genes.fa', 'w')

# print(type(splice))
donor = splice[0:2]
acceptor = splice[2:4]
# print(donor, acceptor)

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
    if re.findall(donor+ '[a-zA-Z]'+ acceptor, gene_dic[keys]):
        # all the splice in one gene, target is a list
        target = re.findall(donor+ '[a-zA-Z]+'+ acceptor, gene_dic[keys])
        # count the number of TATA box
        counter += TATA_counter(target[0])
        new_keys = keys.rstrip() + ' TATA box number: ' + str(counter) + '\n'
        splice_file.write(new_keys)
        splice_file.write(target[0] + '\n')

TATA_file.close()
splice_file.close()