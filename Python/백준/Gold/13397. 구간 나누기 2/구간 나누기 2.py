import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 13397 구간 나누기2

# N: 배열의 크기, M개 이하의 구간 
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 구간의 점수의 최댓값의 최솟값을 구하는 프로그램
# 너무 어려워서 지피티 도움 받음

def divide():
    # left: 최소 점수
    left = 0

    # right: 최대 점수
    right = max(arr) - min(arr)

    # 탐색할 값이 계속 존재
    while left <= right: 
        # mid: 구간 점수의 최대 허용값
        mid = (left + right) // 2

        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

# 이 mid로 구간을 M개 이하로 나눌 수 있는가?
def check(mid):
    count = 1 # 구간의 개수
    min_v = arr[0]
    max_v = arr[0]

    for i in range(1, N):
        min_v = min(min_v, arr[i])
        max_v = max(max_v, arr[i])

        # 현재 구간 점수가 mid 초과하면
        if max_v - min_v > mid:
            count += 1
            min_v = arr[i]
            max_v = arr[i]

    return count <= M

result = divide()
print(result)