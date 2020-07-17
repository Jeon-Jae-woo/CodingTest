# DNA
"""
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
"""

import sys

n, m = map(int, sys.stdin.readline().split(" "))

DNA = []
for i in range(0,n):
    DNA.append(sys.stdin.readline().rstrip())

count = 0
result = []
for i in range(0,m):
    dna_list = dict(A=0,C=0,G=0,T=0)
    for j in range(0,n):
        if DNA[j][i] == 'A':
            dna_list['A'] +=1
        elif DNA[j][i] == 'T':
            dna_list['T'] +=1
        elif DNA[j][i] == 'G':
            dna_list['G'] +=1
        elif DNA[j][i] == 'C':
            dna_list['C'] +=1
    
    max_key = max(dna_list, key=dna_list.get)
    max_value = max(dna_list.values())
    count += n - max_value
    result.append(max_key)

string = ''.join(result)
print(string)
print(count)


