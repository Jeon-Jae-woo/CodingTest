# 2xn 타일링

import sys

n = int(sys.stdin.readline())
arr = [i for i in range(n+1)]
for i in range(3,n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[-1]%10007)