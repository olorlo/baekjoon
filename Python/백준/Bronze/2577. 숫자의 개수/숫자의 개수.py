# 2577번

arr = [int(input()) for _ in range(3)]
num = arr[0] * arr[1] * arr[2]
cnt = [0] * 10
for i in str(num):
    cnt[int(i)]+=1

for i in cnt:
    print(i)