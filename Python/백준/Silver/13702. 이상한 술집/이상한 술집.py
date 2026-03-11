# 백준 13702번 이상한 술집

def binary_search():
    # 막걸리 용량
    left, right = 1, max(size)

    # K명에게 나눠줄 수 있는 최대 막걸리 용량 계산
    while left <= right:
        mid = (left + right) // 2
        
        # K명에게 나눠줄 수 있는지 체크
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