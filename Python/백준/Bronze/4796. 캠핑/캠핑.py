# 백준 4796번
# 캠핑
tc=0
while(True):
    # 테스트 케이스
    tc +=1
    L, P, V =map(int,input().split())
    if L==0 and P ==0 and V ==0:
        break
    # 출력
    print(f'Case {tc}: {(V//P)*L +min(L, V%P)}')