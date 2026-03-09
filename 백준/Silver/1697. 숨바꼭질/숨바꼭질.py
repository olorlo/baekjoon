import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 1697번 숨바꼭질
def bfs(n,k):
    dq = deque([n])
    visited[n] = 0

    while dq:
        subin = dq.popleft()

        if subin == k:
            return visited[subin]
    
        if 0 <= subin*2<=100000 and visited[subin*2] == -1:
            visited[subin*2] = visited[subin] + 1
            dq.append(subin*2)

        if 0 <= subin-1<=100000 and visited[subin-1] == -1:
            visited[subin -1] = visited[subin] + 1
            dq.append(subin-1)

        if 0 <= subin+1 <=100000 and visited[subin+1] == -1:
            visited[subin +1] = visited[subin] + 1
            dq.append(subin+1)
 
N, K = map(int,input().split())
visited = [-1] * 100001
print(bfs(N, K))