def solution(play_list, listen_time):
    answer = 0
    temp_play_list = []

    for i in range(0, len(play_list)):
        temp = listen_time -1
        j = i+1
        count = 1
        while True:
            if temp <= 0:
                temp_play_list.append(count)
                break
            if j >= len(play_list):
                j = 0
            temp = temp - play_list[j]
            count +=1
            
            j +=1
    
    answer = max(temp_play_list)
    if answer >= len(play_list):
        answer = len(play_list)

    return answer




play_list = [1, 2, 3, 4]
listen_time = 5

result = solution(play_list, listen_time)

print(result)

"""
    if sum(play_list) <= listen_time:
        answer = len(play_list)
        return answer
"""