# 볼링공 고르기
# 배열 모든 조합 구하기, but 조합하는 숫자가 같은 경우 제외

#bol = [1,3,2,3,2]
#bol = [1,5,4,3,2,4,5,2]
import sys

N,M = map(int, sys.stdin.readline().split(' '))
data = list(map(int, sys.stdin.readline().split(' ')))
values = 0
for i in range(0, len(data)-1):
	for j in range(i,len(data)):
		if data[i] != data[j]:
			values +=1

print(values)