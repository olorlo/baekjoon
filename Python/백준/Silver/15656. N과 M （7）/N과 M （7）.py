import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 15656번 N과 M(6)
def recur(path):

    # 종료 조건
    if len(path) == M:
        print(*path)
        return 
    
    for i in range(N):
        
        path.append(arr[i])

        recur(path)

        path.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# visited = [0] * N

recur([])