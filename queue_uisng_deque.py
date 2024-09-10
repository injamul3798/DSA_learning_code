# Queue data structure has multiple operations
# enqueue deque

from collections import deque

def is_empty(queue):
    return len(queue) == 0

queue = deque()

# Enqueue operations
queue.append('Injam')
queue.append('231')
queue.append('2342')

print(queue)

# Dequeue operations,Follow the Fifo rules
queue.popleft()
print(queue)

print('is empty: ',is_empty(queue))


