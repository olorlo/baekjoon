import sys
input = sys.stdin.readline
import heapq

# 백준 11279번 최대 힙
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0 and heap:
        # 최대값 출력하고, 그 값을 배열에서 제거함
        print(-heapq.heappop(heap))
    elif x == 0 and not heap:
        print(0)
    else:
        # 최대 힙을 만들기 위해서 음수값을 넣는다.
        heapq.heappush(heap, x * (-1))