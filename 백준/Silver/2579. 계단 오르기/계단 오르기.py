# SWEA 2579번 계단 오르기

num = int(input())
stairs = [0]+[int(input()) for _ in range(num)]

# dp: i번째 계단까지 올라왔을 때 얻을 수 있는 최대 점수
dp = [0] * (num+1)

# 계단이 1개일 때: 그냥 1번 계단 밟기
dp[1] = stairs[1]

# 계단이 2개이상일 때만:
if num >= 2:
    # 처음 밟은 계단이 (2일 때)와 (1일때+2를 밟음) 을 비교
    # -> 당연하게 후자가 더 크다.
    dp[2] = max(stairs[2], stairs[1] + stairs[2])

# 계단이 3이상이고 마지막 계단까지 계산
for i in range(3, num + 1):
    dp[i] = max(
        # 현재의 dp는 현재 계단 + 전전계단까지의 dp
        dp[i-2] + stairs[i], 
        # 현재 계단 + 전 계단 + 전계단의 전전계단까지의 dp를 계산
        dp[i-3] + stairs[i-1] + stairs[i])

print(dp[num])