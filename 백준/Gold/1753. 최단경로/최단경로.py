import sys
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

from collections import deque
import heapq

# 백준 1753번 최단경로
V, E = map(int, input().split())
K = int(input())

def dijkstra(start):
    # (현재까지의 누적 비용, 현재 정점)을 저장할 힙
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0 

    while heap:
        # 현재까지 비용이 가장 작은 정점을 꺼냄
        cost, now = heapq.heappop(heap)

        # 이미 더 짧은 거리로 지금 노드를 방문한 적 있으면 버림 (오래된 정보)
        # distance[now]: 우리가 알고있는 최단 거리(시작점 - 현재 정점)
        if cost > distance[now]:
            continue
        
        # 현재 정점과 연결된 다음 정점 확인
        for next, weight in graph[now]:
            # 현재 정점과 다음 정점을 연결한 간선 비용
            new_cost = weight + cost

            # 새 간선 비용이 기존 최단거리보다 작으면 갱신
            if new_cost < distance[next]:
                distance[next] = new_cost
                # 갱신된 거리 정보를 힙에 넣음 -> 힙에 같은 노드가 여러번 들어갈 수 있음
                heapq.heappush(heap, (new_cost, next))

# 방향 그래프 만들기
graph =[[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단경로를 저장해야하기때문에 초기값은 무한대로 넣는다.
distance = [float('inf')] * (V+1)

dijkstra(K)
for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
        continue
    print(distance[i])