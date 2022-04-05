import sys

# 0,1은 무조건 더하고 나머지는 곱하기하면 최대값

n = sys.stdin.readline().strip()
cal = list(map(int,n))
result = cal[0]

for i in range(1,len(cal)):
    if cal[i] == 1 or cal[i] == 0 or result==0 or result==1:
        result += cal[i]
    else:
        result *=cal[i]


print(result)
        