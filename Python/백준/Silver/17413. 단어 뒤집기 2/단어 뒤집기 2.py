# 백준 17413번 단어 뒤집기 2

S = input()

stack = []
origin = []
i = 0
j=0
mode = False
for a in S:
    if a == '<':
        mode = True
        while stack:
            print(stack.pop(), end= '')
        print(a, end = '')
    elif a == '>': 
        print(a, end = '')
        mode = False
    elif mode == True:
        print(a, end = '')
    elif a == ' ':
        while stack:
            print(stack.pop(), end = '')
        print(end = ' ')
    else:
        stack.append(a)

while stack:
    print(stack.pop(), end = '')