a = 1
b = 1

days= ['SUN','MON','TUE','WED','THU','FRI','SAT']
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_month = 0
for i in range(0, a):
    total_month += month[i]

total_month -= month[a-1]
total_month += b

print(total_month)

day = days[5]
j = 5
for i in range(0, total_month):
    if j == 7:
        j = 0 
    day = days[j]
    j +=1

print(day)