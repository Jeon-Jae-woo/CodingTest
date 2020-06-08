arr = [4,4,4,3,3]
result = []

for i in range(0, len(arr)):
    if arr[i] in result:
        if result[-1] == arr[i]:
            pass
        else:
            result.append(arr[i])
    else:
        result.append(arr[i])

print(result)