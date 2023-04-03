from collections import deque

num_of_actions = int(input())

book_queue = deque()

for n in range(0, num_of_actions):
    action_book_input = input()
    action_and_book_title = action_book_input.split(' ', 1)

    if action_and_book_title[0] == 'BUY':
        book_queue.appendleft(action_and_book_title[1])
    elif action_and_book_title[0] == 'READ':
        print(book_queue.popleft())
