# 백준 11005번 진법 변환2
N, B = map(int, input().split())
result = ''
stack = []

while True:
    stack.append(N % B)
    if N < B :
        break
    N = N//B

while stack:
    s = stack.pop()
    if 0 <= s <=9:
        value = str(s)
    else:
        value = chr(s-10+65)
    result += value

print(result)