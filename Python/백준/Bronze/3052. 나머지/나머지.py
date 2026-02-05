# 3052번
n = [int(input()) for _ in range(10)]
arr = [i % 42 for i in n]

cnt ={}
for j in arr:
    if j in cnt:
        cnt[j] +=1
    else:
        cnt[j] = 0
print(len(cnt))