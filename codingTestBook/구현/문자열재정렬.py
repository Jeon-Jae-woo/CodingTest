import sys
import re

# K1KA5CB7
# AJKDLSI412K4JSJ9D

string = sys.stdin.readline().strip()
number = re.findall("\d",string)
temp = re.findall("[^0-9]", string)
temp.sort()

if len(number) == 0:
    print(''.join(temp))
else:
    value = 0
    for n in number:
        value += int(n)
    temp.append(str(value))
    print(''.join(temp))
