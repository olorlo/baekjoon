import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 2493번 탑
# 핵심: 왼쪽에서 자기보다 처음으로 큰 탑 찾기

N = int(input())
height = list(map(int, input().split()))

stack = []
result = [0] * N
# 시간초과 난 코드
# while True:
#     a= stack.pop()
#     if not stack:
#         result.append(0)
#         break
#     if a > max(stack):
#         result.append(0)
#     else:
#         for i in range(len(stack)-1,-1,-1):
#             if a < stack[i]:
#                 result.append(i+1)
#                 break

for i in range(N):
    h = height[i]

    #현재보다 작은 탑 제거
    while stack and stack[-1][1] < h: 
        stack.pop()

    # 남아있는게 있으면 그게 수신 탑
    if stack:
        result[i] = stack[-1][0] + 1

    # 현재 탑 추가
    stack.append((i,h))

print(*result)