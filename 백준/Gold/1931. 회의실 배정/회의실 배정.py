# 백준 1931번 회의실 배정

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

# 회의 끝나는 시간을 기준으로 정렬
# 빨리 끝나는 회의를 먼저 선택해야 뒤에 많은 회의를 넣을 수 있음
meeting.sort(key = lambda x: (x[1], x[0]))

last_end = 0
cnt = 0

# 회의 시작 시간이 끝나는 시간과 같거나 크면 해당 회의 시작
for i in range(N):
    if meeting[i][0] >= last_end:
        cnt += 1
        last_end = meeting[i][1]

print(cnt)