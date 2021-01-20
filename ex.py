import sys

N = int(sys.stdin.readline().strip())
horror = list(map(int, sys.stdin.readline().split(' ')))

group = 0
person = 0

horror.sort()
for h in horror:
	person +=1
	if person == h:
		group +=1
		person = 0

print(group)