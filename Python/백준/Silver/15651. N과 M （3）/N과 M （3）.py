import sys
# sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

# 백준 15651번 N과 M(3)
def recur(path):
    if len(path) == M:
        print(*path)
        return 
    for i in range(1, N+1):
        path.append(i)
        recur(path)
        path.pop()

N, M = map(int, input().split())

visited = [0] * (N + 1)
recur([])