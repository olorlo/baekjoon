import sys
input = sys.stdin.readline
# 백준 1647 도시 분할 계획

# N: 집의 수, M: 집을 연결하는 길의 수
N, M = map(int, input().split())

# 알고리즘(유니온 파인드)
# MST를 만든 다음에 가장 비싼 간선만 제거

# union_find
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

# 그래프 만들기
edges = []
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
# 가장 큰 비용을 빼기 위해서 정렬해줌
edges.sort()

# 자기 자신이 대표자인 집합 만듦
parents = [i for i in range(N+1)]

total, max_cost = 0, 0
for cost, a, b in edges:
    # 같은 집합이 아니라면 같은 집합으로 만들어주기
    rep_x = find_set(a)
    rep_y = find_set(b)

    if rep_x != rep_y:
        parents[rep_x] = rep_y
        total += cost
        max_cost = cost # 마지막 가장 큰 비용 저장

print(total - max_cost)