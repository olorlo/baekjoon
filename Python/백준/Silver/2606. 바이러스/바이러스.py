import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 2606번 바이러스

n = int(input())
pair = int(input())
arr = [list(map(int, input().split())) for _ in range(pair)]

visited = [0] * (n+1)

def bfs(start):
    global cnt
    dq = deque([start])
    visited[start] = 1

    while dq:
        now = dq.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            cnt+=1 
            dq.append(next)


graph = [[] for _ in range(n+1)]

cnt = 0

# 그래프 만들기
for i, j in arr:
    graph[i].append(j)
    graph[j].append(i)

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
bfs(1)
print(cnt)