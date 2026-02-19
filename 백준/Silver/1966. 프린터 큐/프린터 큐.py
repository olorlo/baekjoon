from collections import deque

# 백준 1966번 프린터 큐

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    
    cnt = 0

    for i in range(N):
        queue.append((arr[i],i))

    while len(queue) >= 1:
        
        # 큐에서 꺼낸 요소가 우선순위가 제일 크면 꺼낸다 
        max_queue = max(x[0] for x in queue)
        a = queue.popleft()
        if a[0] == max_queue:
            cnt += 1 
            if a[1] == M:
                print(f'{cnt}')
                break
        
        # 우선순위가 제일 크지 않으면 다시 넣음
        else:
            queue.append(a)