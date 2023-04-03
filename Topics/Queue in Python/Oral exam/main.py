from collections import deque

n = int(input())

my_queue = deque()

while n > 0:
    el_to_queue = input().split(" ")
    if el_to_queue[0] == 'READY':
        my_queue.appendleft(el_to_queue[1])
    elif el_to_queue[0] == 'EXTRA':
        my_queue.appendleft(my_queue[len(el_to_queue)])
        my_queue.pop()
    else:
        print(my_queue.pop())
    n -= 1

