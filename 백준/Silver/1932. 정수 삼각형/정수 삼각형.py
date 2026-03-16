import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline 

# 백준 1932번 정수삼각형
n = int(input())

# 삼각형의 높이만큼 주어짐
triangle = [list(map(int, input().split())) for _ in range(n)]

# dp를 2차원 배열로 만들어야한다.
# dp: 이 위치까지 올 수 있는 최대값
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = triangle[0][0]

# 삼각형 위에서부터 내려오자
# 초기값은 dp[0] == 7로 설정함

for i in range(1, n):

    for j in range(i+1):

        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
print(max(dp[n-1]))