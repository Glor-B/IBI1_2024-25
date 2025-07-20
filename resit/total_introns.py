import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
total_intron = re.findall(r'(?=(GT.*AG))', seq) + re.findall(r'(?=(GT.*?AG))', seq)
print(total_intron)