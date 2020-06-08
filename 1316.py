# 1316
n = int(input())

if n >=100:
    exit()

count = 0
compare = []
for i in range(0,n):
    string = input().lower()
    
    if string in compare:
        exit()

    compare.append(string)
    temp = []
    for j in range(0,len(string)):
        if string[j] in temp and j != 0:
            if temp[j-1] != string[j]:
                break
        temp.append(string[j])
        if j == len(string)-1:
            count +=1

print(count)

