def solution(s):
    length = []
    result = ""
    len_2=len(s)//2+1
    
    for cut in range(1, len_2): 
        count = 1
        temp = s[:cut] 
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""

                result += str(count) + temp
                temp = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp
        length.append(len(result))
        result = ""
    
    if len(length) == 0:
        length.append(1)

    return min(length)



s = "a"

ans = solution(s)

print(ans)