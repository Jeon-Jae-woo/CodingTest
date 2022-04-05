# 5622
string = input().upper()

if 2>len(string) or 15<len(string):
    exit()

count = 0
for i in range(0, len(string)):
    if string[i] in 'ABC':
        count +=3
    if string[i] in 'DEF':
        count +=4
    if string[i] in 'GHI':
        count +=5
    if string[i] in 'JKL':
        count +=6
    if string[i] in 'MNO':
        count +=7
    if string[i] in 'PQRS':
        count +=8
    if string[i] in 'TUV':
        count +=9
    if string[i] in 'WXYZ':
        count +=10

print(count)
