# ATM 

import sys

n = int(sys.stdin.readline())
person = list(map(int, sys.stdin.readline().split(' ')))

if n < len(person):
    exit()
sum=0
total=0
person.sort()
for i in range(0, len(person)):
    sum += person[i]
    total += sum

print(total)