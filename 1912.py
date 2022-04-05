# max값 저장후 갱신
# 10 -4 3 1 5 6 -35 12 21 -1
# 계단오르기, 포도주와 비슷함 , 연속 규칙은 존재하지 않으므로 점화식이 필요 없을듯?
# - 가 존재해서 지금 값 보다 작으면 필요없음

import sys

n = int(sys.stdin.readline())

number = [0 for i in range(n)]
number = list(map(int,sys.stdin.readline().split()))

temp = number[0]
max_value = temp

if len(number) == 1:
    print(max_value)
    exit()

for i in range(1,len(number)):
    temp = max(temp+number[i], number[i])
    if temp >= max_value:
        max_value = temp

print(max_value)






