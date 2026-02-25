# 백준 2992번 크면서 작은 수

X = input()
orig = int(X)
arr = list(X)

visited = [False] * len(X)
path = []

answer = float('inf')

def recur():
    global answer

    # path가 X 길이와 같으면 숫자 조합
    if len(path) == len(X):
        num = int(''.join(path))
        # 만든 숫자가 더 크면 그 중 가장 작은 값 저장
        if num > orig:
            answer = min(answer, num)
        return
    
    # X 중 방문되지 않은 곳이 있다면 방문하고 path에 추가 
    for i in range(len(X)):
        if visited[i] == False:
            visited[i] = True
            path.append(X[i])

            recur()

            path.pop()
            visited[i] = False

recur()
# 만든 숫자보다 큰 값이 없는 경우 무한대
if answer == float('inf'):
    print(0)
else:
    print(answer)
