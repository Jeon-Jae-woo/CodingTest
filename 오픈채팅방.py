def solution(record):
    user = {}
    log = [] # 2차원 배열 
    answer = []
    for i in range(0,len(record)):
        slice_value = record[i].split(' ')
        if len(slice_value) > 2:
            user[slice_value[1]] = slice_value[2]
        
        log.append(slice_value[:2])

    for i in range(0, len(log)):
        if log[i][0] == 'Enter':
            answer.append(user[log[i][1]]+"님이 들어왔습니다.")
        elif log[i][0] == 'Leave':
            answer.append(user[log[i][1]]+"님이 나갔습니다.")
    
    return answer





record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = solution(record)
print(result)