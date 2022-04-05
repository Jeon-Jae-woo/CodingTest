"""
def solution(bricks):
    answer = 0
    
    select = bricks[0]
    index = 0 # 다음 인덱스면
    n = 0 # 벽돌
    count = 0 # 칸수
    water = 0 # 총 물칸
    for i in range(1,len(bricks)):
        if select <= bricks[i] and index+1 == i:
            select = bricks[i]
            continue
        if select <= bricks[i]:
            water += (select*count)-n
            print('water' , water)
            n = 0
            count = 0
            index = i
            select = bricks[i]
        else:
            n += bricks[i]
            count +=1

    answer = water
    return answer


bricks = [0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0]

result = solution(bricks)

print(result)
"""


def solution(bricks):
    answer = 0
    temp = "".join(map(str, bricks))
    temp = temp.strip("0")
    bricks = list(map(int, temp))

    count = 0 # 칸수
    water = 0 # 총 물칸
    
    for i in range(1, max(bricks)+1):
        count = 0
        check = False
        print('i')
        for j in range(0, len(bricks)):
            if j+1 != len(bricks) and bricks[j] >= i and bricks[j+1] >= i:
                continue
            if bricks[j] >= i:
                if check is True:
                    print('cehck')
                    check = False
                    if j+1 != len(bricks) and bricks[j+1] <= i:
                        check = True
                    water += count
                    count = 0
                    print('check')
                else:
                    check = True
            elif check is False:
                continue
            else:
                count +=1
                print('count',count)

    print(water)
    return answer


# 2, 0, 1, 3, 1, 2, 0, 1, 0, 2
bricks = [0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0]
result = solution(bricks)

#print(result)