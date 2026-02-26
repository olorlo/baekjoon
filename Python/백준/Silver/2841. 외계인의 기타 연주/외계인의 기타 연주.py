import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 2841번 외계인의 기타 연주

N, P = map(int, input().split())

finger = [[] for _ in range(7)]

cnt = 0

for _ in range(N):
    num, fret = map(int, input().split())

    # 프렛 보다 큰 값 존재하면 없애기
    while finger[num] and finger[num][-1] > fret:
        finger[num].pop()
        cnt += 1

    # 같은 프렛이면 아무것도 안함      
    if finger[num] and finger[num][-1] == fret:
        continue

    finger[num].append(fret)
    cnt += 1

print(cnt)