# 백준 1182번 부분 수열의 합

N, S = map(int, input().split())
cnt = 0 
arr = list(map(int, input().split()))

def recur(idx, s):
    global N, S, cnt
    if idx == N:
        if s == S:
            cnt +=1
        return
    
    # 선택하는 경우
    recur(idx+1, s + arr[idx])

    # 선택 안하는 경우
    recur(idx+1,s)
    
recur(0, 0)

# 공집합인 경우
if S ==0:
    cnt -= 1
print(cnt)