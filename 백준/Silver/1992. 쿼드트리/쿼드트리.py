# 백준 1992번 쿼드트리
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def comp(a):

    sum_a = 0
    len_a = 0

    for i in a:
        for j in i:
            sum_a += j
            len_a += 1

    # print('sum_a:', sum_a)
    # print('len_a:', len_a)

    # 전체가 1로 이루어져있다면 1 출력
    if sum_a == len_a:
        print(1, end='')
        return 

    # 전체가 0으로 이루어져있다면 0 출력
    elif sum_a == 0:
        print(0, end='')
        return

    # 전체에서 0과 1이 섞여있으면 4등분으로 나눔
    else:
        print('(', end='')
        size = len(a) // 2
        # 왼쪽 위
        b=[[] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                b[i].append(a[i][j])
        comp(b)
        
        # 오른쪽 위
        d=[[] for _ in range(size)]
        for i in range(size):
            for j in range(size, len(a)):
                d[i].append(a[i][j])
        comp(d)
        
        # 왼쪽 아래
        c=[[] for _ in range(size)]
        for i in range(size, len(a)):
            for j in range(size):
                c[i-size].append(a[i][j])
        comp(c)
        
        # 오른쪽 아래
        e=[[] for _ in range(size)]
        for i in range(size, len(a)):
            for j in range(size, len(a)):
                e[i-size].append(a[i][j])
        comp(e)
        print(')', end='')
        
comp(arr)