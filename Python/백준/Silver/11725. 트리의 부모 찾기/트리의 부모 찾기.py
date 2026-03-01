import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 백준 11725번 트리의 부모 찾기
N = int(input())
arr = [[] for _ in range(N+1)]

# 부모 찾아서 넣는 리스트
result = [0] * (N+1)

# 방문했는지 확인하는 리스트
visited = [0] * (N+1)

# 양방향 그래프 입력
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

def recur(node):
    # 현재 노드 방문 처리
    visited[node] = 1
    
    # 현재와 연결된 다음 노드가 방문되지 않았다면, 
    # 부모노드로 처리하고 다음 노드로 이동
    for next in arr[node]:
        if not visited[next]:
            result[next] = node
            recur(next)

# 트리의 루트를 1이라고 정함
recur(1)

# 결과 출력
for i in range(2, N+1):
    print(result[i])