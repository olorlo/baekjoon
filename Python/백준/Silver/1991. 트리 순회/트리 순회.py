import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 백준 1991번 트리 순회

N = int(input())
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

# 순회 결과를 저장할 리스트
preorder = []
inorder = []
postorder = []


def recur(node):
    # 자식이 없는 경우: 리턴
    if node == '.':
        return 
    
    # 전위순회: 뿌리부터 왼쪽, 오른쪽
    preorder.append(node)

    # 왼쪽 자식으로 이동
    recur(tree[node][0])

    # 중위순회: 왼쪽, 뿌리, 오른쪽
    inorder.append(node)

    # 오른쪽 자식으로 이동
    recur(tree[node][1])

    # 후위순회: 왼쪽, 오른쪽, 뿌리
    postorder.append(node)


recur('A')
for i in range(N):
    print(preorder[i], end = '')
print()
for i in range(N):
    print(inorder[i], end = '')
print()
for i in range(N):
    print(postorder[i], end = '')
