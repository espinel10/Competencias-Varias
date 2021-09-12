def solve(t):
    N=int(input().strip())
    S=input().strip()
    S=S.replace("F","")
    cont=0
    if len(S)==0:
        print("Case #{}: {}".format(t,cont))
        return 
    ant=S[0]
    for i in S:
        if ant!=i:
            ant=i
            cont+=1
    print("Case #{}: {}".format(t,cont))


T=int(input().strip())
for _ in range(T):
    solve(_+1)