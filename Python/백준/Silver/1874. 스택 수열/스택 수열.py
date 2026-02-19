# 백준 1874번 스택 수열
n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
result = []
ans = []
idx = 0
i = 1
while True:

    if result == arr:
        break

    
    while stack:
        if arr[idx] == stack[-1]:
            result.append(stack.pop())
            ans.append('-')
            # print('-')
            idx += 1
        else: 
            break

    if i >= n + 1:
        break
    stack.append(i)
    # print('+')
    ans.append('+')
    i += 1

if result == arr:
    for i in ans:
        print(i, end = '\n')
else:
    print('NO')