# len(orders[i]) - course + 1:
# j + co + 1
# 2 번
def solution(orders, course):
    answer = []
    for co in course:
        food = {}
        for i in range(0, len(orders)):
            orders[i] = ''.join(sorted(orders[i]))
            for j in range(0, len(orders[i])-co+1):
                x = j
                while True:
                    if x == len(orders[i])-1 or x == len(orders[i])-co+1:
                       break
                    temp = orders[i][j]
                    for z in range(0,co-1):
                        temp += orders[i][x+z+1]
                    if temp in food:
                        food[temp] +=1
                    else:
                        food[temp] = 1
                    x+=1
        if not food:
            continue
        max_value = max(food.values())
        for key, value in list(food.items()):
            if value == 1:
                food.pop(key)
            elif value == max_value:
                answer.append(key)

    answer.sort()
    return answer





orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]		

result = solution(orders, course)

print(result)