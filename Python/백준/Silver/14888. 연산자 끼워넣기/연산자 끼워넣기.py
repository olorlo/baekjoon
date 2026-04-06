# import sys
# sys.stdin = open("input.txt", "r")

# 백준 파이썬 14888번 연산자 끼워넣기

# 입력
N = int(input())
arr = list(map(int, input().split()))
oper0 = list(map(int, input().split()))

# 변수 선언
max_result = -float('inf')
min_result = float('inf')

def cal(oper_num, now, result, oper):
    global max_result, min_result
    
    # 종료 조건: 연산자(oper_num)를 다 썼을 때
    # 최대, 최소 값 저장
    if oper_num == 0:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    # 들어갈 때: oper_num -1
    for i in range(len(oper)):
        if oper[i]:
            if i == 0:
                # operator = '+'
                oper[i] -= 1
                cal(oper_num-1, now+1, result + arr[now+1], oper)
                oper[i] += 1 
            elif i == 1:
                # operator = '-'
                oper[i] -= 1
                cal(oper_num-1, now+1, result - arr[now+1], oper)
                oper[i] += 1 
            elif i == 2:
                # operator = '*'
                oper[i] -= 1
                cal(oper_num-1, now+1, result * arr[now+1], oper)
                oper[i] += 1 
            else:
                # operator = '/'
                oper[i] -= 1
                if result <0:
                    cal(oper_num-1, now+1, -(-result // arr[now+1]), oper)
                else:
                    cal(oper_num-1, now+1, result // arr[now+1], oper)
                oper[i] += 1 

cal(N-1, 0, arr[0], oper0)

print(max_result)
print(min_result)