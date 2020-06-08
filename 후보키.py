relation = [["100","ryan","music","2"],
["200","apeach","math","2"],["300","tube","computer","3"],
["400","con","computer","4"],["500","muzi","music","3"],
["600","apeach","music","2"]]

leng = len(relation[0])
leng2 = len(relation)
arr = [['']*leng2 for _ in range(leng)]
count = 0
temp = []
for i in range(0,len(relation)):
    for j in range(0,leng):
        arr[j][i] = relation[i][j]

for i in range(0, len(arr)):
    if len(arr[i]) != len(set(arr[i])):
        temp.append(arr[i])
    else:
        count +=1

if len(temp) >= 2:
    leng3 = len(temp[0])
    for i in range(0,len(temp)):
        for j in range(0,):
        

print(count)



"""
can_list = 0
temp_list = []
temp = ''
for j in range(0,leng):
    for i in range(0,len(relation)):
        if temp == relation[i][j]:
            temp_list.append('1')
            break
        else:
            temp = relation[i][j]
            if j == len(relation)-1:
                can_list +=1        

print(can_list)
"""