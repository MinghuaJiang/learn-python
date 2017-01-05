from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Ben")
queue.append("Helen")

print queue

print queue.popleft()

print queue