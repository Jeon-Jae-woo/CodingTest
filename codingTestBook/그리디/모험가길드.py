# 공포도 X
# 최대 그룹 만들기
# N = 모험가 수
# 사람수 == 공포도 -> 그룹 +1
import sys

n = int(sys.stdin.readline())
person = list(map(int, sys.stdin.readline().split(' ')))
person.sort()
group = 0
count = 0

for per in person:
    count +=1
    if per == count:
        group +=1
        count = 0
    
print(group)