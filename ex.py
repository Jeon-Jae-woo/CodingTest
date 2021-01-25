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
