import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 15654번 N과 M(5)
def recur(path):

    # 종료 조건
    if len(path) == M:
        print(*path)
        return 
    
    for i in range(N):
        # 이미 방문: continue
        if visited[i]:
            continue

        # 방문하지 않았다면: 방문 표시
        if not path or path[-1] <=arr[i]:
            visited[i] = True
            path.append(arr[i])

            recur(path)

            path.pop()
            visited[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N

recur([])