from collections import deque

# 백준 1021번 회전하는 큐
N, M = map(int, input().split())
location = list(map(int, input().split()))
cnt = 0
queue = deque()

for i in range(N):
    queue.append(i+1)

for x in location:
    idx = queue.index(x)
    # 왼쪽으로 돌리기
    if idx <= len(queue)//2:
        queue.rotate(-idx)
        cnt += idx
    # 오른쪽으로 돌리기
    else:
        queue.rotate(len(queue) - idx)
        cnt += len(queue) - idx
    queue.popleft()

print(cnt)
        