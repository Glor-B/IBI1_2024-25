import re

# Get the input & donor and acceptor
splice = input('Choose and enter the splice donor/acceptor combination (GTAG/GCAG/ATAC):',)
# print(type(splice))
donor = splice[0:2]
acceptor = splice[2:4]
# print(donor, acceptor)

# open file needed
genome = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# TATA_file = open('TATA_genes.fa', 'w')
splice_file = open(str(splice) + '_spliced_genes.fa', 'w')

# dictionary to store gene name and gene information with noncoding sequences
gene_dic = {}
# output = re.split(r'>', genome)
# i = 1

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
    # to test, so limit the for loop time    
    '''i += 1
    if i == 100000:
        break'''
    
""" for keys in gene_dic:
    new_keys = re.sub('gene:', '>', keys)
    new_keys = re.sub(' ', '\n', new_keys)       
    splice_file.write(new_keys)
    splice_file.write(str(gene_dic[keys]) + '\n')
#print(gene_dic) """

""" def intron_counter(seq):
    if splice == 'GTAG':
        total_intron = re.findall(r'(?=(GT.*AG)', seq) + re.findall(r'?=(GT.*?AG))', seq)
    elif splice == 'GCAG':
        total_intron = re.findall(r'(?=(GC.*AG)', seq) + re.findall(r'?=(GC.*?AG))', seq)
    elif splice == 'ATAC':
        total_intron = re.findall(r'(?=(AT.*AC)', seq) + re.findall(r'?=(AT.*?AC))', seq)                                                                                                 
    num = len(total_intron)
    return(num) """

# find sequence with target splice
for keys in gene_dic:
    seq = gene_dic[keys]
    if splice == 'GTAG':
        total_intron = re.findall(r'(?=(GT.*AG))', seq) + re.findall(r'(?=(GT.*?AG))', seq)
    elif splice == 'GCAG':
        total_intron = re.findall(r'(?=(GC.*AG))', seq) + re.findall(r'(?=(GC.*?AG))', seq)
    elif splice == 'ATAC':
        total_intron = re.findall(r'(?=(AT.*AC))', seq) + re.findall(r'(?=(AT.*?AC))', seq)
    else:
        print('Wrong input')
        break
    counter = len(total_intron)
    #if re.findall(donor + '[a-zA-Z]+'+ acceptor, gene_dic[keys]):
        # all the splice in one gene, target is a list
        # target = re.findall(donor + '[a-zA-Z]+'+ acceptor, gene_dic[keys])
        # count the number of TATA box
    new_keys = re.sub('gene:', '>', keys)
    new_keys = re.sub(' ', '\n', new_keys)  
    new_keys = new_keys.rstrip() + ' Possible intron number: ' + str(counter) + '\n'
    splice_file.write(new_keys)
    splice_file.write(gene_dic[keys] + '\n')

splice_file.close()