import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 15651번 N과 M(4)
def recur(path):
    if len(path) == M:
        print(*path)
        return 
    
    for i in range(1, N+1):
        if path:
            if path[-1] <= i:
                path.append(i)
                recur(path)
                path.pop()
        else:
            path.append(i)
            recur(path)
            path.pop()

N, M = map(int, input().split())

recur([])
        