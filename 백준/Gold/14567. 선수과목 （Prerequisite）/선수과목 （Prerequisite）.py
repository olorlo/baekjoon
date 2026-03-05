import sys
# sys.stdin = open("python/input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    max_sem = 0
    if visited[node]:
        return visited[node]
    max_sem = 0
    for next in graph[node]:
        max_sem = max(max_sem, dfs(next))
    visited[node] = max_sem + 1
    return visited[node]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

for i in range(N+1):
    dfs(i)

print(*visited[1:])