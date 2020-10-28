mod=10**9+7
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    initans=1
    finarray=[0]*(n+1)
    finalsol=[]
    for i in range(n,0,-1):
        finarray[i]=initans
        initans=((initans%mod)*2)%mod
    #print(finarray)
    for i in a:
        finalsol.append(finarray[i])
    print(*finalsol)
    
"""
l=[[]]
final=[2,1,3,4]
for i in final:
    k=[]
    for j in l:
        k.append(j+[i])
    l.extend(k)
sol=[0]*5
for i in l[1:]:
    sol[min(i)]+=1
print(sol)
"""

"""
def findpow(a,b):
    remainderB=0
    for i in range(len(b)):
        remainderB=(remainderB*10+ord(b[i])-48)%(mod-1)
    res=1
    x=a%mod
    while(remainderB>0):
        if remainderB&1:
            res=(res*x)%mod
        remainderB>>=1
        x=(x*x)%mod
    return res
"""
    
