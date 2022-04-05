import sys
"""
           -1,-1  -1,0  -1,+1
            0,-1 [?][?]  0,+1
           +1,-1  +1,0  +1,+1

           방문한 곳을 0으로 바꿈 ?
           빈 리스트 만들고 8개 좌표값 다 넣음 -- 값이 1인 경우 확장 필요
           1,0 여부는 알 수 없음 그냥 다 0으로 만들고 리턴
           범위 벗어나면 넘어감
"""

def search(graph, x, y): # x = h , y = w
    temp_list = []
    temp_list.append([x,y]) # 초기값
    while temp_list:
        temp_x, temp_y = temp_list.pop()
        if 0>temp_x or temp_x>=h: # 범위 체크
            continue 
        if 0>temp_y or temp_y>=w: # 범위 체크
            continue
        if graph[temp_x][temp_y] == 0: # 0이면 건너뜀
                    continue

        graph[temp_x][temp_y] = 0 # 방문 0 으로 만들기

        # temp_list에 x,y 8개 좌표 모두 저장
        temp_list.append([temp_x-1,temp_y-1])
        temp_list.append([temp_x-1,temp_y])
        temp_list.append([temp_x-1,temp_y+1])
        temp_list.append([temp_x,temp_y-1])
        temp_list.append([temp_x,temp_y+1])
        temp_list.append([temp_x+1,temp_y-1])
        temp_list.append([temp_x+1,temp_y])
        temp_list.append([temp_x+1,temp_y+1])

    return

result = []
while(1):
    w, h = map(int, sys.stdin.readline().split(' '))
    if w + h == 0:
        break

    graph = []
    for i in range(0,h):
        graph.append(list(map(int, sys.stdin.readline().split(' '))))

    count = 0
    for i in range(0,h): # row y
        for j in range(0,w): # col x
            if graph[i][j] == 0:
                continue
            else:
                count +=1
                search(graph, i, j)
    result.append(str(count))

print('\n'.join(result))