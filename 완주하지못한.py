"""
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

if 1 > len(participant) < 100000:
    exit()
if len(completion) != len(participant)-1:
    exit()
string = ''
for arr in completion:
    if arr in participant:
        pass
    else:
        string = arr

if string = '':
    

print(string)
"""

"""
def solution(participant, completion):
    if 1 > len(participant) < 100000:
        exit()
    if len(completion) != len(participant)-1:
        exit()
    
    for arr in completion:
        if arr in participant:
            participant.remove(arr)

    answer = ''.join(participant)
    return answer
"""
"""
n = 2
m = 5

answer = []
for i in range(n+1,1,-1):
    if n%i==0 and m%i==0:
        max_value=i
        break
    else:
        max_value=1
answer.append(max_value)
answer.append(n*m//max_value)

print(answer)
"""

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

if 1 > len(participant) < 100000:
    exit()
if len(completion) != len(participant)-1:
    exit()
    
result = []
string = ''
for arr in participant:
    if arr in result:
        string = ''.join(arr)
        break
    result.append(arr)
    if arr in completion:
        pass
    else:
        string = ''.join(arr)
        break

answer = string
print(answer)