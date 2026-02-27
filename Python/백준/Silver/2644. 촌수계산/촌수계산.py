import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 2644번 촌수계산

# n: 사람 수 
n = int(input())

# p1, p2: 촌수를 계산해야하는 두 사람의 번호
p1, p2 = map(int, input().split())
p = [p1, p2]

# m: 관계의 수 
m = int(input())

# relation: 양방향 그래프
# 인덱스: 부모 / 값: 자식 
relation = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    relation[y].append(x)
    relation[x].append(y)

# print(relation) # [0, 0, 1, 1, 0, 4, 4, 2, 2, 2]

# 이미 부모를 찾은 사람을 넣음
found = [0] * (n+1)
cnt = 0
find_p = 0

# 자식의 부모를 찾는 dfs 
def find(now, depth):
    global cnt, find_p
    
    if now == find_p:
        return depth

    # 현재 자식의 부모 찾음
    found[now] = 1

    # 다음으로 이동
    for next in relation[now]:
        if not found[next]:
            result = find(next, depth + 1)
            # result 가 -1이라는 것은 p2를 못찾음
            # result가 -1이 아니면! result = depth
            if result != -1:
                return result
            
    # p2를 못찾았음 -> -1 반환
    return -1

# 사람 수만큼 dfs 돌리기
# 부모를 못찾았고, 부모가 존재한다면
for i in range(2):
    if not found[p[i]] and relation[p[i]]:
        # 그 부모로 들어간다.
        if i == 0:
            find_p = p2
        else:
            find_p = p1
        ans = find(p[i], 0)
        print(ans)
        break

