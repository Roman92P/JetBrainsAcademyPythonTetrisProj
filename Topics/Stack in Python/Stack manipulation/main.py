from collections import deque

my_stack = deque()

n = int(input())

while n > 0:
    operation = str(input())
    arr = operation.split(" ")
    if arr[0] == 'PUSH':
        my_stack.append(arr[1])
    elif arr[0] == 'POP':
        my_stack.pop()
    n -= 1

my_stack.reverse()
for i in my_stack:
    print(i)
