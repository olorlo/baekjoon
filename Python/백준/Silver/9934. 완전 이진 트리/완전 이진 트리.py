import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 백준 9934번 완전 이진 트리
K = int(input())
n = 2**K - 1
arr = list(map(int, input().split()))

tree = [[] for _ in range(K)]

def inorder(start, end, depth):
    # 종료조건
    if start > end:
        return
    
    mid = (start + end) // 2

    tree[depth].append(arr[mid])

    # print(arr[idx])
    inorder(start, mid - 1, depth + 1)
    inorder(mid + 1, end, depth + 1)
    
inorder(0, n-1, 0)

for i in tree:
    print(*i)