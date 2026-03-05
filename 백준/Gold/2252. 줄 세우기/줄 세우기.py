import sys
# sys.stdin = open("python/input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

# 백준 2252번 줄 세우기

# 위상 정렬
# 1. indegree 계산
# 2. indegree 0 큐
# 3. 하나씩 꺼냄
# 4. 연결노드 indegree 감소
# 5. 0되면 큐



N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# indegree: 나보다 먼저 와야하는 사람의 수
# -> indegree가 0 이면 바로 줄 설 수 있다.
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    # 노드로 들어오는 간선의 개수 세기
    indegree[B] += 1

def bfs():
    dq = deque()

    # 차수가 0인 것만 덱에 넣는다.
    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        print(now, end = ' ')

        # 나랑 연결되어있는 내 뒤에 있을 사람 골라서 indgree 하나 감소시킴 
        # -> indegree가 0일 경우 줄 세움
        for next in graph[now]:
            indegree[next] -= 1
            # 간선의 개수가 0 이다 -> 내 앞에 아무도 없다.
            # 바로 줄 설 수 있음 dq로 줄 세운다.
            if indegree[next] == 0:
                dq.append(next)

bfs()