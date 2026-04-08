import heapq

# SWEA 최소 이동 거리
T = int(input())

def connect(node):
    dist = [float('inf')] * (N+1)
    dist[node] = 0
    
    # 힙 만들기
    heap = [(0, node)]
    
    while heap:
        now_dist, now_node = heapq.heappop(heap)
        
        # 이미 더 짧은 거리로 방문한 적 있으면 건너뛰기
        if dist[now_node] < now_dist:
            continue
        
        # 힙에 다음 노드 넣기
        for next_node, weight in graph[now_node]:        
            new_dist = now_dist + weight
            
            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    return dist[N]

for tc in range(1, T+1):
    # N: 마지막 연결 지점 번호
    # E: 도로의 개수
    N, E = map(int, input().split())
    
    # 구간 시작 s, 구간의 끝점 e, 구간 거리 w 
    arr = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 만들기
    graph = [[] for _ in range(N+1)]
    for s, e, w in arr:
        graph[s].append((e, w))
        
    # 방문했는지 체크
    visited = [0] * (N+1)

    # 함수 실행
    result = connect(0)
    
    print(f'#{tc} {result}')