import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 14889 스타트와 링크
# -> swea 요리사 문제랑 비슷
N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]


# 1. 일단 스타트와 링크로 나누기
# 2. 나눈 팀에서 능력치 계산
# 3. 능력치의 최소값 계산

min_val = float('inf')

# 팀 나누기
def assign(now, start):
    global min_val 

    if len(start) == N//2:
        link = []
        for i in range(N):
            if i in start:
                continue
            link.append(i)

        value = abs(cal(start)-cal(link))
        min_val = min(min_val, value)
        return
    
    for next in range(now, N):
        start.append(next)
        assign(next+1, start)
        start.pop()

def cal(team):
    total = 0

    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a = team[i]
            b = team[j]

            # 모든 팀원 조합 경우의 수 계산
            total += S[a][b] + S[b][a]

    return total

assign(0, [])

print(min_val)