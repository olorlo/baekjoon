# 백준 1018번
# 체스판 다시 칠하기
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 100

# 보드를 체스판으로 잘라내기
for a in range(N-7):
    for b in range(M-7):
        cnt = 0
        for i in range(a,a+8):
            for j in range(b, b+8):
                # 검사: 좌표 합이 홀수, 짝수인지에 따라 색이 달라진다. 
                if (i+j) % 2==0: # 시작색
                    # W로 시작한다고 대충 가정함. 
                    if arr[i][j] != 'W':
                        cnt += 1
                else: # 반대색
                    if arr[i][j] != 'B':
                        cnt += 1
        # 대충 가정한 cnt의 반대가 정확히 B로 시작하는 경우임 
        # 제일 작은 값 찾아서 반환
        result = min(result, cnt, 64 - cnt)     

# for i in range(N):
#     print(*arr[i])
print(result)