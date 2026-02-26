# 백준 9935번 문자열 폭발

# rstrip(): 오른쪽 끝 공백과 enter 제거하는 함수 
arr = input().rstrip()
bomb = input().rstrip()

stack = []
len_bomb = len(bomb)
idx = 0

for i in arr:
    # 한 글자씩 stack에 push
    # 문자를 하나씩 추가할 때마다 폭발 검사 
    stack.append(i)

    # stack길이가 bomb보다 크거나 같고, stack의 끝이 bomb이면 
    # stack[-len_bomb:] 이면 뒤에서 len_bomb개만큼 가져오겠다 
    if len(stack) >= len_bomb and stack[-len_bomb:] == list(bomb):
        # bomb 길이만큼 stack pop
        # -> stack에는 폭발 후 문자열만 남는다.
        for _ in range(len_bomb):
            stack.pop()

result = ''.join(stack)    
    
print(result if result else "FRULA")