


queue_list = []
priorities = [1, 1, 9, 1, 1, 1]
location_list = [0 for i in range(len(priorities))]
location = 0
location_list[location] = 1

count = 0
while(priorities):
    i = 0
    max_value = max(priorities)
    if max_value == priorities[i]:
        count +=1
        del priorities[i]
        if location_list[i] != 1:
            del location_list[i]
        else:
            print(count)
            break
    else:
        priorities.append(priorities[i])
        del priorities[i]
        location_list.append(location_list[i])
        del location_list[i]


