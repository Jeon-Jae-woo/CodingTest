# 뒤집기

# 001100
# 구간별로 나눔 00, 11, 00 -> count 0 - 2, 1 - 1 
# 작은수 출력

import sys

number = sys.stdin.readline().strip()

zero = 0
one = 0
temp = 2
for i in range(0,len(number)):
    if temp != number[i]:
        temp = number[i]
        if number[i] == '0':
            zero +=1
        elif number[i] == '1':
            one +=1

result = zero if zero < one else one
print(result)

