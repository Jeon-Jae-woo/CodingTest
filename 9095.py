# 1,2,3 더하기

# 값이 4 부터는 -1,-2,-3 까지 경우의 수 합


import sys

count = int(sys.stdin.readline())
number = [0 for i in range(12)]

number[1] = 1 # 1
number[2] = 2 # 2
number[3] = 4 # 3

while count:
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        number[i] = number[i-1]+number[i-2]+number[i-3]
    print(number[n])
    count -=1