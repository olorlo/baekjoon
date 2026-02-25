# 백준 2630번 색종이 만들기
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
cnt_blue = 0
cnt_white = 0

def cut(start_row, end_row, start_col, end_col):
    global cnt_blue, cnt_white
    sum_arr = 0
    len_arr = 0
    for i in range(start_row,end_row+1):
        for j in range(start_col, end_col+1):
            sum_arr += arr[i][j]
            len_arr += 1

    if sum_arr == 0:
        cnt_white += 1
        return 
    elif sum_arr == len_arr:
        cnt_blue += 1
        return
    
    mid_row = (end_row + start_row) // 2
    mid_col = (end_col + start_col) // 2
    # 왼쪽 위
    cut(start_row, mid_row, start_col, mid_col)
    # 오른쪽 위
    cut(start_row, mid_row, mid_col+1, end_col)
    # 왼쪽 아래
    cut(mid_row+1, end_row, start_col, mid_col)       
    # 오른쪽 아래
    cut(mid_row+1, end_row, mid_col+1, end_col)

    return cnt_white, cnt_blue

cut(0, N - 1, 0, N - 1)    
print(cnt_white)
print(cnt_blue)