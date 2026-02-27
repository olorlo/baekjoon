import sys
# sys.stdin = open("python/input.txt", 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 11724번 연결 요소의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)
cnt = 0

def recur(v):

    visited[v] = 1
    # 다음 연결된 정점으로 이동
    for next in graph[v]:
        if not visited[next]:
            recur(next)

# 방향 없는 그래프 만들기 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 순회
for i in range(1, N+1):
    if not visited[i]:
        recur(i)
        cnt+=1

print(cnt)