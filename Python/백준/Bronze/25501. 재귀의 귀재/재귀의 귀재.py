# 백준 25501번
T = int(input())

def recursion(s, l, r):
    global cnt
    if (l >= r ):
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt
    cnt +=1
    return recursion(s,0, len(s)-1)
for i in range(1,T+1):
    cnt = 0
    S = input()
    result = isPalindrome(S)
    print(result, cnt)