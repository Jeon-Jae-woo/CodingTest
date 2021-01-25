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


"""
import sys

string = sys.stdin.readline().strip()
numbers = '0123456789'
data = []
result = 0
for i in range(0,len(string)):
	if string[i] in numbers:
		result += int(string[i])
	else:
		data.append(string[i])
data.sort()
data.append(str(result))

print(''.join(data))

"""
