def solution(flowers):
    result = []
    answer = 0
    for i in range(0,len(flowers)):
        for j in range(flowers[i][0], flowers[i][1]):
            result.append(j)

    answer = len(set(result))
    
    return answer



#flowers = [[2,5],[3,7],[10,11]]
flowers = [[3,4],[4,5],[6,7],[8,10]]

an = solution(flowers)

print(an)


