import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 11722 가장 긴 감소하는 부분 수열
N = int(input())
A = list(map(int, input().split()))

# 자기 자신을 포함하기 때문에 1
dp = [1]*N

# 자기 자신 위치에서 그 전 인덱스들을 비교함

for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))
