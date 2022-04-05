# 잃어버린 괄호
import sys

n = sys.stdin.readline().strip()
string = n.split('-')

for i in range(0,len(string)):
    result = 0
    if '+' in string[i]:
        temp = string[i].split('+')
        for j in range(0,len(temp)):
            result += int(temp[j])
        string[i] = result
    else:
        string[i] = int(string[i])

min_value=string[0]

for i in range(1,len(string)):
    min_value = min_value - string[i]

print(min_value)