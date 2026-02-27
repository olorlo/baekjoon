import sys
# sys.stdin = open("python/input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 11403번 경로 찾기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

result = [[0] * N for _ in range(N)]

# 인접 행렬 dfs 구현 
# visited를 위해서 함수 실행
def dfs(v):
    # v 방문 표시
    visited[v] = 1
    # 다음 v 찾기
    # 만약 인접 행렬에서 1 이 존재하고 방문되지 않았다면 이동 
    for next in range(N):
        if arr[v][next] == 1 and visited[next] == 0:
            dfs(next)

# 돌때마다 visited를 초기화 시켜준다. 
for start in range(N):
    visited= [0] * N
    
    for next in range(N):
        if arr[start][next] == 1 and visited[next] == 0:
            dfs(next) # -> 처음꺼 돌려서 방문한 정점 모두 visited에 저장됨

    # 모든 정점에 대해서 방문된 정점이 있으면 result 1로 만들어준다.
    for end in range(N):
        if visited[end]:
            result[start][end] = 1

for i in result:
    print(*i)