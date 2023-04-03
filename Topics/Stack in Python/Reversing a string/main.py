from collections import deque

n = int(input())

my_stack = deque()

while n > 0:
    el = input()
    my_stack.appendleft(el)
    n -= 1

for i in my_stack:
    print(i)
