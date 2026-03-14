# 백준 2745번 진법 변환
N, B = input().split()
B = int(B)
result = 0 

for i in range(len(N)):
    if '0' <= N[i] <='9':
        value = int(N[i])
    else:
        value = ord(N[i]) - ord('A') + 10
    result += value * (B ** (len(N) - 1 -i))

print(result)