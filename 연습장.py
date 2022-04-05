n = 12345 
string = str(n)
answer = []
for i in range(0,len(string)):
    answer.append(int(string[i]))

print(answer)
answer.reverse()
print(answer)