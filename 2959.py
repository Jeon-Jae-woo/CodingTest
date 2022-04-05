import sys

turtle = list(map(int, sys.stdin.readline().split(' ')))
turtle.sort()
print(turtle.pop(0)*turtle.pop(-2))