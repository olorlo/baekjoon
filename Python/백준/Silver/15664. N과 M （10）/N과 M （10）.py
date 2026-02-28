import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 15664번 N과 M(10)
def recur(path, start):

    # 종료 조건
    # 깊이: len(path)
    if len(path) == M:
        print(*path)
        return 
    
    # prev: 현재 깊이에서 중복이 있는지 체크하기 위한 변수
    # -> 깊이마다 따로 존재해야함 따라서 depth 시작 시 초기화
    prev = -1

    # 현재 깊이에서 선택할 수 있는 후보들 
    for i in range(start,N):
        # print(visited)
        if visited[i]:
            continue
        
        # 중복인지 검사
        if arr[i] == prev:
            continue
       
        visited[i] = 1
        path.append(arr[i])

        # [1,9]가 두번 나오지 않게 중복 제거
        prev = arr[i]
        recur(path, i)

        path.pop()
        visited[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * (N)

recur([], 0)