# 점프 점프

# dp[j+maze[i]]
# dp에는 해당 칸까지 오는데 필요한 횟수중 가장 적은 횟수를 넣는다

# 미로를 1중 반복, 2중 반복에 dp 현재 길이까지 반복 ? 
# for i in range(0, len(dp???))
# dp[i+j] 는 해당 위치에 존재하는 최소값임, dp[i]+1은 지금 칸에서 해당 칸으로 넘어간 경우의 값 즉 둘 중에 최소값을 찾으면 해당 자리에는 최소로 올 수 있는 숫자가 들어가게됨 dp[i+j] = dp[i] + 1
# 1 2 0 1 3 2 1 5 4 2
import sys

n = int(sys.stdin.readline().strip())
maze = list(map(int, sys.stdin.readline().split(' ')))
dp = [1001]*(n)

dp[0] = 0

for i in range(0, len(maze)):
    if maze[i] == 0:
        continue
    for j in range(1,maze[i]+1):
        if i+j <= len(dp)-1:
            if dp[i+j] > dp[i]+1: # i,j 는 범위 체크
                dp[i+j] = dp[i]+1


if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])