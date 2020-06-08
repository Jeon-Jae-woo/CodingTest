# 1157 
string = input('').upper()

if len(string) > 1000000:
    exit()

exdict = {}

# 카운트
for i in range(0, len(string)):
    if string[i] in exdict:
        exdict[string[i]] +=1
    else:
        exdict[string[i]] = 1
print(exdict)
# max 찾기
temp = 0
for key ,value in exdict.items():
    if temp < value:
        maxK = key
        temp = value

# max 값 2개 이상
values = list(exdict.values())
if values.count(max(values)) >= 2:
    print("?")
else:
    print(maxK)
