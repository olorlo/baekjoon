import sys, copy
from itertools import permutations
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 배열 돌리기4

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# for _ in range(K):
#     r, c, s = map(int, input().split())
oper = [list(map(int, input().split())) for _ in range(K)]

# 우하좌상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 회전하는 함수
def spin(r, c, s, A):
    r -= 1
    c -= 1

    for layer in range(1, s+1):
        top = r - layer
        bottom = r + layer
        left = c - layer
        right = c + layer

        prev = A[top][left]

        # 위쪽 테두리
        for i in range(left+1, right+1):
            A[top][i], prev = prev, A[top][i]

        # 오른쪽 테두리
        for i in range(top+1, bottom+1):
            A[i][right], prev = prev, A[i][right]
        
        # 아래 테두리
        for i in range(right-1, left-1, -1):
            A[bottom][i], prev = prev, A[bottom][i]

        # 왼쪽 테두리
        for i in range(bottom-1, top-1, -1):
            A[i][left], prev = prev, A[i][left]

min_A = float('inf')

# oper 리스트 내 회전 연산 수 만큼 회전 연산을 한번씩 사용
# 순열 사용
for perm in permutations(oper, K):
    A = copy.deepcopy(arr)

    for r, c, s in perm:
        spin(r, c, s, A)
    
    for row in A:
        min_A = min(min_A, sum(row))

# for row in A:
#    print(row)
print(min_A)