# 큰 수의 법칙
import sys

# M번 더함, k번 연속
N,M,K = map(int, sys.stdin.readline().split(' '))
data = list(map(int, sys.stdin.readline().split(' ')))

data.sort(reverse=True)
result = 0

temp = 0
while True:
    if M == 0:
        break
    M -=1
    temp +=1
    if temp > K:
        temp = 0
        result +=data[1]
    else:
        result +=data[0]
        

print(result)