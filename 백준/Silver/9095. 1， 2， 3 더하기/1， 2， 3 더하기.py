# 백준 9095번
# 1,2,3 더하기

T = int(input())

dp =[0]*12
def recur(num):
    if dp[n]:
        return dp[n]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        dp[num] = recur(num-1) + recur(num-2) + recur(num-3)
        return dp[num]
    

for _ in range(T):
    result = 0
    n = int(input())
    print(recur(n))