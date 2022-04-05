
array = [1, 5, 2, 6, 3, 7, 4] # 6
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
temp = []

for i in range(0,len(commands)):
    temp = array[(commands[i][0]-1):commands[i][1]]
    temp.sort()
    answer.append(temp[commands[i][2]-1])
   
print(answer)



# if commands[i][1] == len(array):
#        temp = array[commands[i][0]-1:]
#    else: