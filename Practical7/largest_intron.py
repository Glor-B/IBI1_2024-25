import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT[a-zA-Z]+AG', seq)
print(largest_intron)