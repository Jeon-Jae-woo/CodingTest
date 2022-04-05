# N이 K로 나눠지는 경우 나누고 Count++ -> 나머지가 0인 경우
# N이 K로 나눠지지 않는 경우 -1 , Count++ -> 나머지가 존재하는 경우

import sys

n, k = map(int, sys.stdin.readline().split(" "))
count = 0

while True:
    if n==1:
        break
    if n%k == 0:
        n = n/k
        count +=1
    else:
        n = n-1
        count +=1
    
print(count)


