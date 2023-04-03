from collections import deque

n = int(input())

my_queue = deque()

while n > 0:
    el = input().split(" ")
    action = el[0]
    if action == "ENQUEUE":
        my_queue.appendleft(el[1])
    elif action == "DEQUEUE":
        my_queue.pop()
    n -= 1

my_queue.reverse()

for i in my_queue:
    print(i)
