import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 2193 이친수
N = int(input())

dp = [0]*(N+1)

dp[1] = 1

if N >=2:
    dp[2] = 1

for n in range(3, N+1):
    # 끝이 0이면 아무거나 붙이기 + 끝이 1이면 0뒤에만 붙이기
    dp[n] = dp[n-1] + dp[n-2]

print(dp[N])
