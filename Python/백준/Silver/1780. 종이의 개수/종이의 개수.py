# 백준 1780번 종이의 개수
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_minus1 =0
cnt_0 = 0
cnt_1 = 0

# r: 시작 행
# c: 시작 열
# size: 현재 종이 한 변의 길이
def cut(r, c, size):

    global cnt_minus1, cnt_0, cnt_1

    compare = arr[r][c] 

    # 같은 숫자인지 확인
    for i in range(r, r + size):
        for j in range(c, c + size):
            # 다를 때 
            if arr[i][j] !=compare:
                new = size // 3
                for dr in range(3):
                    for dc in range(3):
                        cut(r + dr * new, c + dc * new, new)
                return
            
    if compare == -1:
        cnt_minus1 += 1
    elif compare == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1

cut(0, 0, N)
print(cnt_minus1)
print(cnt_0)
print(cnt_1)