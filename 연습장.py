priorities = [2, 1, 3, 2]
location = 2
answer = 0
from collections import deque

d = deque([(v,i) for i,v in enumerate(priorities)])
print(d)
print(max(d)[0])
while len(d):
  item = d.popleft()
  if d and max(d)[0] > item[0]:
      d.append(item)
  else:
      answer += 1
      if item[1] == location:
          break
