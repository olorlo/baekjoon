# 백준 1920번 수찾기
N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

def binary_search(target):
    # A 리스트 인덱스
    left, right = 0, N-1

    while left <= right:
        mid = (left + right) // 2

        if check(mid, target):
            left = mid + 1
        else:
            right = mid - 1
    return left -1

def check(mid, target):
    # cnt = 0
    
    if B[target] >= A[mid]:
        return True
    return False

for i in range(M):
    result = binary_search(i)
    if B[i] == A[result]:
        print(1)
    else:
        print(0)
