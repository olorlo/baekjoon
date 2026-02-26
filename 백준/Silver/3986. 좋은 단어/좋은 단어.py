# 백준 3986번 좋은 단어

stack = []

N = int(input())

arr = [list(input()) for _ in range(N)]
cnt = 0

for i in arr:
    stack = []
    for j in range(0, len(i)):

        # 스택 존재하면 그 전에껄 꺼내서 현재랑 비교 
        # - 만약 같으면 
        # - 같지 않으면 다시 넣고 현재꺼도 넣기
        # 존재하지 않으면 그냥 현재꺼 추가만 하기 
        if stack: 
            s2 = stack.pop()
            if i[j] == s2:
                continue
            else:
                stack.append(s2)
                stack.append(i[j])

        else:
            stack.append(i[j])

    if not stack:
        cnt += 1

print(cnt)