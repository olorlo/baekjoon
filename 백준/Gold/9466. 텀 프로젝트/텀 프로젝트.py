import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# 백준 9466번 텀 프로젝트

T = int(input())

def dfs(node):
    global result

    # 방문 처리 후 사이클에 해당 노드 추가
    visited[node] = 1
    cycle.append(node)
    
    # 현재와 연결되어있는 next 찾음
    next = students[node]

    # 만약 next가 방문되지 않은 새 정점이라면 dfs 돌린다
    if not visited[next]:
        dfs(next)

    # 만약 cycle 돌아서 돌아왔다면(방문 되었다면)
    # 사이클 내에 next가 있는지 확인 -> 사이클인지 확인
    # 사이클이면   
    # 1. 사이클 시작 위치 찾기
    # 2. 그 위치부터 사이클 끝까지 잘라서 사이클 길이 재기
    
    else:
        if next in cycle:
            start = cycle.index(next)
            team = cycle[start:]
            result += len(team)

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [0] * (n+1)
    result = 0
    
    # cycle 수를 세고 전체에서 빼기
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n-result)