# 백준 1654번 랜선 자르기
# == 13702번 이상한 술집 문제랑 같은듯?

def binary_search():
    left, right = 1, max(size)

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left -1

def check(mid):
    r = 0
    for cup in size:
        r += cup//mid
    if r >= K:
        return True
    return False


N, K = map(int, input().split())

size = [int(input()) for _ in range(N)] 

result = binary_search()

print(result)