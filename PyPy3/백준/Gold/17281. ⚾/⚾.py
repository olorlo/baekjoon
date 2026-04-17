import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 17281 야구

# 이닝 수
inning = int(input())
# 각 선수가 각 이닝에서 얻는 결과
# 안타: 1, 2루타: 2, 3루타: 3, 홈런: 4, 아웃: 0
arr = [list(map(int, input().split())) for _ in range(inning)]

visited = [0] * 9
max_score = 0

# 타순 결정
def decide(team):
    global max_score

    if len(team) == 9:
        score = simulation(team)
        max_score = max(max_score, score)
        return
    
    # 4번 타자가 무조건 0번 선수
    if len(team) == 3:

        # 0번 선수를 4번 타자에 추가한다.
        team.append(0)
        decide(team)
        team.pop()
        return

    # 1~8만 사용
    for i in range(1, 9):
        if visited[i]:
            continue

        # 일반 경우: 4번 타자 자리가 아닐 때
        visited[i] = 1
        team.append(i)
        decide(team)
        team.pop()
        visited[i] = 0

def simulation(team):
    score = 0
    batter_idx = 0 # 현재 타자 위치

    for i in range(inning):
        inning_result = arr[i]
        out = 0
        b1, b2, b3 = 0, 0, 0 # 1루, 2루, 3루

        while True:
            # 현재 플레이어: 현재 타자위치
            player = team[batter_idx]
            result = inning_result[player]

            batter_idx = (batter_idx+1)%9
            # 아웃
            if result == 0:
                out += 1
                if out == 3:
                    break
            
            # 안타
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2

            # 2루타
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1

            # 3루타
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1

            # 홈런
            elif result == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

    return score

visited[0] = 1
decide([])
print(max_score)