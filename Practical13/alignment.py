import blosum as bl
import re
matrix = bl.BLOSUM(62)

def seq_reader(seq):
    gene_sequence = ''
    for line in seq:
        if re.search(r'>', line):
            continue
        else:
            gene_sequence += line.rstrip()
            seq = gene_sequence
    return seq

SOD2_human = seq_reader(open("P04179.fasta.txt"))
SOD2_mouse = seq_reader(open("P09671.fasta.txt"))
random = seq_reader(open("random.fasta"))

def seq_compare(seq1, seq2):
    edit_distance = 0 
    score = 0
    percentage = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            edit_distance += 1 
        score += matrix[seq1[i]][seq2[i]]
    percentage = (len(seq1) - edit_distance ) / len(seq1) * 100
    print('Edit distance:', edit_distance)
    print('Alignment score:', score)
    print('Percentage of identical amino acids:', round(percentage, 2), '%\n')

print('Comparison between SOD2_human and SOD2_mouse:')
seq_compare(SOD2_human, SOD2_mouse)
print('Comparison between SOD2_human and random sequence:')
seq_compare(SOD2_human, random)
print('Comparison between SOD2_mouse and random sequence:')
seq_compare(SOD2_mouse, random)