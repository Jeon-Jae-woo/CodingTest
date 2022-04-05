first=[1,2,3,4,5] * 2000# 2000
second=[2,1,2,3,2,4,2,5] * 1250 # 1250
third=[3,3,1,1,2,2,4,4,5,5] * 1000 # 1000


answers = [1,3,2,4,2]
count_list = {1:0,2:0,3:0}

for i in range(0,len(answers)):
    if first[i] == answers[i]:
        count_list[1] +=1
    if second[i] == answers[i]:
        count_list[2] +=1
    if third[i] == answers[i]:
        count_list[3] +=1

answer = []
max_value = max(count_list.values())
for key, value in count_list.items():
    if max_value == value:
        answer.append(key)

answer.sort()

print(answer)