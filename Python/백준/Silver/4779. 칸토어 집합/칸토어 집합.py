# 백준 4779번 칸토어 집합

def recur(start, end):
    interval = (end-start+1) // 3
    if interval < 1:
        return 

    for j in range(interval):
        current[start+interval+j] = ' '
    # 남은 '-' 들
    recur(start, start + interval - 1)
    recur(start + 2*interval, end)
    
    return current

while True:
    try:
        N = int(input())
        current = ['-']*(3**N)
        recur(0, 3 ** N - 1)
        print(''.join(current))
        
    except EOFError:
        break