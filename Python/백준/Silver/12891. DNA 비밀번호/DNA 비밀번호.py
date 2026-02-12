S, P = map(int, input().split())
DNA = input()
condition = list(map(int, input().split())) 
cnt = [0] * 4
result = 0

def idx(c):
    if c =='A': return 0
    if c =='C': return 1
    if c =='G': return 2
    if c =='T': return 3

# 제일 처음 윈도우 
for i in range(P):
    cnt[idx(DNA[i])] += 1

if cnt[0] >= condition[0] and cnt[1] >= condition[1] \
    and cnt[2] >=condition[2] and cnt[3] >= condition[3]:
    result += 1


for i in range(S-P):
    cnt[idx(DNA[i])] -= 1
    cnt[idx(DNA[i+P])] += 1
        
    if cnt[0] >= condition[0] and cnt[1] >= condition[1] \
        and cnt[2] >=condition[2] and cnt[3] >= condition[3]:
        result += 1
print(result)