def bt(path):
    if len(path) == M:
        print(*path)
        return 
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            path.append(i)
            bt(path)
            path.pop()
            visited[i] = 0    

N, M = map(int, input().split())

visited = [0] * (N+1)
bt([])
