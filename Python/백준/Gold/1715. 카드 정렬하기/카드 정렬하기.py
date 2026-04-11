import heapq

# 백준 1715번 카드 정렬하기

# N개의 숫자 카드 묶음
N = int(input())

def card():
    heap = []

    for c in arr:
        heapq.heappush(heap, c)

    result = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        sum_val = a+b
        result += sum_val
        
        heapq.heappush(heap, sum_val)

    return result

arr = [int(input()) for _ in range(N)]

answer = card()
print(answer)