from collections import deque

# 백준 2161번 카드1

N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while len(queue) > 0 :
    print(queue.popleft(), end=' ')
    if queue:
        queue.append(queue.popleft())