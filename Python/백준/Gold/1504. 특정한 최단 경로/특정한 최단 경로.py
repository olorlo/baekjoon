import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

import heapq

# 백준 1504 특정한 최단 경로

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1번 정점에서 N번 정점으로 이동할 때, 
# 주어진 두 정점을 반드시 거치면서 최단 경로로 이동


def move(start):
    distance = [float('inf')]*(N+1)
    distance[start] = 0 

    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)

        # 여기까지 온 비용이 distance내 저장되어있는 최소값보다 크면 
        # 비교할 필요도 없다
        if distance[now] < cost:
            continue
           
        for next, dist in graph[now]:
            new_cost = cost + dist

            if distance[next] > new_cost:
                distance[next] = new_cost
                heapq.heappush(heap, (new_cost, next))
                
    return distance
dist1 = move(1)
dist_v1 = move(v1)
dist_v2 = move(v2)

case1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
case2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

result = min(case1, case2)

# 갈 수 없는 경우 처리
if result >= float('inf'):
    print(-1)
else:
    print(result)
