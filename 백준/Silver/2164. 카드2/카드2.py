from collections import deque

# 백준 2164번 카드2

N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while len(queue) > 1 :
    queue.popleft()
    if queue:
        queue.append(queue.popleft())
print(queue.popleft())