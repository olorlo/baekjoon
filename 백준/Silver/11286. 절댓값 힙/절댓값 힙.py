import sys
input = sys.stdin.readline 
import heapq

# 백준 11286번 절댓값 힙

heap = []

N = int(input())
for i in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
            continue
        a, b = heapq.heappop(heap)
        if b == -1:
            print(-a)
        else:
            print(a)
       
    else:
        if x < 0:
            heapq.heappush(heap, (-x, -1))
        else:
            #  x가 양수일때
            heapq.heappush(heap, (x, 1))