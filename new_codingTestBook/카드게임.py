import sys

n, m = map(int, sys.stdin.readline().split(" "))

min_value = 0
for i in range(n):
    data = list(map(int, sys.stdin.readline().split(" ")))
    temp = min(data)
    if min_value<temp:
        min_value = temp



print(min_value)