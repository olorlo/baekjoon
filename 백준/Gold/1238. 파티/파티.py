import sys
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

from collections import deque
import heapq

# 백준 1238번 파티
N, M, X = map(int, input().split())

def dijkstra(s, g):
    # 힙 생성
    heap = []
    heapq.heappush(heap, (0, s))
    distance = [float('inf')]*(N+1)
    distance[s] = 0

    while heap:
        cost, now = heapq.heappop(heap)
        
        # 오래된 값 버리기
        if cost > distance[now]:
            continue
    
        for next, weight in g[now]:
            new_cost = weight + cost
            if new_cost < distance[next]:
                distance[next] = new_cost

                heapq.heappush(heap, (new_cost, next))
    return distance

graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    reversed_graph[end].append((start, time))

max_sum = 0

d = dijkstra(X, graph)
r_d = dijkstra(X, reversed_graph)

for i in range(1, N+1):
    max_sum = max(d[i] + r_d[i], max_sum)

print(max_sum)