import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT[a-zA-Z]+AG', seq)
counter = re.split(r'.', largest_intron[0])
#print(counter)
length = len(counter) - 1
print(largest_intron, length)