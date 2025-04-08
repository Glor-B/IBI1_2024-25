import re

sequence = input('Enter your target DNA sequence:')
cut_sites = input('Enter restriction enzyme recognition sequence:')

def input_check(sequence):
    a = re.findall('[A|T|C|G]', sequence)
    if len(a) != len(sequence):
        return False
    else:
        return True
#print(input_check(cut_sites))

def cut(sequence, cut_sites):
    output = []
    if re.search(cut_sites, sequence):
        #return True
        for i in range(0, len(sequence) - len(cut_sites)):
            if sequence[i: i+len(cut_sites)] == cut_sites:
                output.append(i+1)
        return output
    else: 
        return 'No restriction enzyme cut sites'
    #print(cut(sequence, cut_sites))

if input_check(sequence) and input_check(cut_sites):
    print(cut(sequence, cut_sites))
else:
    print('Please ensure that you enter the right DNA sequence.')