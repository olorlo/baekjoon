import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 백준 1068번 트리
# 어떤 노드를 삭제했을 때 남는 리프 노드 개수는 몇개인가?
# 노드를 삭제하면 변하는 것: 그 노드 + 노드의 모든 자식들 
# (중요!) 부모가 자식을 하나 잃으면 그 부모가 리프가 될 수 있음
N = int(input())

parent = list(map(int, input().split()))
child = [[] for _ in range(N)]
delete_node = int(input())
root = 0

# parent가 값인 리스트를 child가 값인 리스트로 바꿈
for i in range(N):
    # 부모가 -1이면 root
    if parent[i] == -1:
        root = i
    else:
        child[parent[i]].append(i)

cnt = 0

def leaf(node):
    global cnt

    if node == delete_node:
        return
    
    # 삭제된 노드를 제외한 자식 개수
    valid_children = 0

    # 자식 개수를 세는 반복문
    for next in child[node]:
        if next == delete_node:
            continue

        valid_children += 1
        leaf(next)
    
    # 자식 개수를 셌는데도 0이다 -> leaf임
    if valid_children == 0:
        cnt += 1

leaf(root)

print(cnt)