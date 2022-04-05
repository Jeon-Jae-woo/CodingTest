# 한 row에 대해서 밑에 row에 값을 더해보고 가장 큰 값을 집어 넣는다 ??
# 시작점 j가 같으면 패스

# 마지막인 경우 들어가지 않고 끝내야 함,


# 16
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

for i in range(1, len(land)):
    for j in range(0, len(land[i])):
        land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

max_value = max(land[-1])

print(max_value)