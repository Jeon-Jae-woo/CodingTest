import sys


N = sys.stdin.readline().strip()
N_list = list(map(int,N))

first = N_list[:int(len(N)/2)]
second = N_list[int(len(N)/2):]

sum1 = sum(first)
sum2 = sum(second)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

"""
import sys

n = sys.stdin.readline().strip()

data = list(map(int,n))
half = int(len(data)/2)
value1 = sum(data[:half])
value2 = sum(data[half:])

if value1 == value2:
	print("LUCKY")
else:
	print("READY")
"""
