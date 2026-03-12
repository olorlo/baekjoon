import sys
input = sys.stdin.readline 
import heapq

# 백준 1927번 최소 힙
heap = []
N = int(input())
for i in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
            continue
        a = heapq.heappop(heap)
        print(a)
    else:
        heapq.heappush(heap, x)