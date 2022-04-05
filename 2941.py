# 2941 
import re
string = input().lower()

if len(string) > 100:
    exit()

croatia = re.compile('c=|c-|dz=|d-|lj|nj|s=|z=')
result = croatia.sub(' ', string)

print(len(result))
