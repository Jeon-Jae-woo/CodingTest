# 만들 수 없는 금액
# 3 2 1 1 9

# sort 이용 - 1 1 2 3 9

# 1원부터 시작해서 만들 수 있는지 검증 - 현재 코인이 money보다 크다면 만들 수 없는 값임
# coin + money 보다 1작은 값 까지 만들 수 있음 

import sys

n = int(sys.stdin.readline())
coin = list(map(int,sys.stdin.readline().split(' ')))
coin.sort()
money = 1

for c in coin:
    if money < c:
        break
    money += c

print(money)