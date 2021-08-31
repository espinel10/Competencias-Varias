
def solve(t,S):
    if len(set(S))==1:
        print("Case #{}: {}".format(t,0))
        return 
    v=[]
    c=[]
    V=['A','E','I','O','U']
    for s in S:
        if s in V:
            v.append(s)
        else:
            c.append(s)

    if len(v)>0 and len(c)>0:
        cons=max(set(c), key=c.count)
        vowel=max(set(v), key=v.count)
        cost1=(len(c)-c.count(cons))*2+len(v)
        cost2=len(c)+(len(v)-v.count(vowel))*2
        resp=min(cost1,cost2)
        print("Case #{}: {}".format(t,resp))
    elif len(v)>0:
        print("Case #{}: {}".format(t,len(v)))
    elif len(c)>0:
        print("Case #{}: {}".format(t,len(c)))

T=int(input().strip())
for _ in range(T):
    S=input().strip()
    solve(_+1,S)
