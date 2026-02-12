# 백준 10025번 게으른 백곰
MAX = 1000000
N, K = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

arr = [0] * (MAX + 1)
for i in range(N):
    arr[ice[i][1]]+=ice[i][0]

if 2 * K >= MAX:
    max_ice = sum(arr)

# 초기 상태 지정
temp = sum(arr[:2*K + 1])

max_ice = temp
for i in range(MAX - 2 * K):
    temp = temp - arr[i] + arr[i + 2 * K+1] 

    max_ice = max(temp, max_ice)

print(max_ice)