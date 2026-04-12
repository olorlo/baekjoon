import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 17070 파이프 옮기기 1
# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 
# 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

# 해당 위치로 갈 수 있는 경우의 수
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 0: 가로, 1: 세로, 2: 대각선
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        for d in range(3):

            now = dp[i][j][d]
            if now == 0:
                continue

            # 가로이면 이동할 수 있는 방법: 가로, 대각선
            if d == 0:
                # 가로
                if j+1 < N and home[i][j+1] == 0:
                    dp[i][j+1][d] += now

                # 대각선
                if i+1 < N and j+1 < N and \
                    home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0:
                    dp[i+1][j+1][2] += now
                

            # 세로이면 이동할 수 있는 방법: 세로, 대각선
            elif d == 1:
                # 세로
                if i+1 < N and home[i+1][j] == 0:
                    dp[i+1][j][d] += now

                # 대각선
                if i+1 < N and j+1 < N and \
                    home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0:
                    dp[i+1][j+1][2] += now

            # 대각선: 가로, 세로, 대각선
            elif d == 2:
                # 가로
                if j+1 < N and home[i][j+1] == 0:
                    dp[i][j+1][0] += now

                # 세로
                if i+1 < N and home[i+1][j] == 0:
                    dp[i+1][j][1] += now

                # 대각선 
                if i+1 < N and j+1 < N and \
                    home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0:
                    dp[i+1][j+1][d] += now

print(sum(dp[N-1][N-1]))