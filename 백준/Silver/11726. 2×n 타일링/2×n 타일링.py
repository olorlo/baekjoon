import sys
input = sys.stdin.readline 

# 백준 11726번 2xn 타일링
# 사실은 피보나치 수열이엇던 것이엇던 것이엇다. 

n = int(input())

dp = [0]*(1+n)

# 초기값 설정
dp[1] = 1

# 런타임 에러 때문에 추가함
if n >=2:
    dp[2] = 2 

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])