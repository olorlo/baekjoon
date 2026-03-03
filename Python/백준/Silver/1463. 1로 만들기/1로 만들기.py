import sys
input = sys.stdin.readline

# 백준 1463번 1로 만들기
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):

    # i에서 1을 빼는 연산을 먼저 고려
    dp[i] = dp[i-1] + 1

    # i가 2로 나누어 떨어지면, 
    # (i//2에서 1로 가는 최소 횟수) + 1(+1을 해주는 이유는 2배 연산하는 게 1이기 때문) 과 비교
    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # i가 3으로 나누어 떨어지면,
    # (i//3에서 1로 가는 최소 횟수) + 1과 비교
    if i % 3 ==0:
        dp[i] = min(dp[i], dp[i//3]+1)

# N을 1로 만드는 최소 연산 횟수
print(dp[N])