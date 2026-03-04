import sys
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

from collections import deque
import heapq

# 백준 1916번 최소비용 구하기
def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0
    
    while heap:
        # 힙에서 가장 cost 작은게 먼저 나온다.
        cost, now = heapq.heappop(heap)

        # cost가 개클 때 스킵 -> 이전거리와 더해볼 필요도 없이 잘라냄
        if cost > distance[now]:
            continue
        
        # cost가 현재 거리보다 더 짧을때 현재거리와 더해서 그래도 더 짧은지 비교해봄
         
        # - 다음 weight와 현재 cost를 더해서 새로운 최단거리를 만든다.
        # - 그 최단 거리가 distance보다 짧을때 
        # - distance로 갱신해주고 힙에다가 다음 노드를 넣음 
        for next, weight in graph[now]:
            new_cost = weight + cost

            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(heap, (new_cost, next))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] 

# 다익스트라는 더 짧으면 갱신이므로 처음값이 0 이면 갱신이 안된다.
distance = [float('inf')] * (N+1)

for _ in range(M):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))

a, b = map(int,input().split())

dijkstra(a)

print(distance[b])