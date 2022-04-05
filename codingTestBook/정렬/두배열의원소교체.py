# K번의 연산을 통해 list_A에 합이 최대가 최도록 수행
"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
import sys

N,K = map(int, sys.stdin.readline().strip().split())

list_A = list(map(int,sys.stdin.readline().strip().split()))
list_B = list(map(int,sys.stdin.readline().strip().split()))

list_A = sorted(list_A)
list_B = sorted(list_B, reverse=True)

for i in range(0,K):
    if list_A[i] < list_B[i]:
        list_A[i] = list_B[i]

value = sum(list_A)

print(value)
