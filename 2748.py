# 피보나치 2
import sys

n = int(sys.stdin.readline())
fibo_list = [i for i in range(n+1)]

for i in range(2,n+1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]


print(fibo_list[-1])



