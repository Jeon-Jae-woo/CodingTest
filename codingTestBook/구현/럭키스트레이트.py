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