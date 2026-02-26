# 백준 5397번 키로거

T = int(input())
for tc in range(T):
    stack = []
    wait = []
    L = list(input())
    for i in range(len(L)):
        # 왼쪽 화살표 라면 스택 존재확인 후 wait에 넣음
        if L[i] == '<':
            if stack:
                wait.append(stack.pop())
        elif L[i] == '>':
            if wait:
                stack.append(wait.pop())
        # 백스페이스라면
        elif L[i] == '-':
            if stack:
                stack.pop()
        # 알파벳이라면
        else:
            stack.append(L[i])

    # wait에 남아있는 알파벳 뒤집어서 stack에 넣어주기
    stack.extend(reversed(wait))

    # 결과 출력
    print(''.join(stack))