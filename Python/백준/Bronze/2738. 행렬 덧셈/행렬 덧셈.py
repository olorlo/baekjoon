# 2738번
N, M = map(int, input().split())
A= [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result =[]
for i in range(N):
    result1 = []
    for j in range(M):
        result1.append(A[i][j]+B[i][j])
    result.append(result1)
for i in result:
    print(*i)