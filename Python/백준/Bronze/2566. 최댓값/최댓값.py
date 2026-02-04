#최대값
n=[]
for i in range(9):
    n.append(list(map(int, input().split())))
n_max=0
for i in n:
    for j in i:
        if j > n_max:
            n_max=j
print(n_max)
for i in range(1,10):
    for j in range(1,10):
        if n[i-1][j-1] == n_max:
            print(i, j)