from collections import deque

# 백준 1158번 요세푸스 문제
N, K = map(int, input().split())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

print('<', end ='')
while len(queue)>1:
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    print(f'{queue.popleft()}', end = ', ')
print(queue.popleft(), end='')
print('>')