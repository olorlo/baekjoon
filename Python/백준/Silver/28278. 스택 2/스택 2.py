import sys
# sys.stdin = open("input.txt", 'r')
# 빠른 입력
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# 백준 28278번 스택2
N = int(input())
stack = []
result = []
for _ in range(N):
    a = list(map(int,input().split()))

    if a[0] == 1:
        stack.append(a[1])

    elif a[0] == 2:
        if stack:
            result.append(stack.pop())

        else:
            result.append(-1)

    elif a[0] == 3:
        result.append(len(stack))
        
    elif a[0] == 4:
        if stack:
            result.append(0)
        else: 
            result.append(1)

    elif a[0] == 5:
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print('\n'.join(map(str,result)))