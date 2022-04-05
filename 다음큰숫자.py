n = 15
count_n = str(bin(n)).count('1')

while True:
    n += 1
    result_n = str(bin(n)).count('1')
    if count_n == result_n:
        result = n
        break


print(result)
