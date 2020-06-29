mod=1000000007

def findfactors(x):
    prod=1
    a={1:1}
    while(x%2==0):
        if 2 not in a:
            a[2]=0
        a[2]+=1
        x//=2
    for i in range(3,x+1,2):
        while(x%i==0):
            if i not in a:
                a[i]=0
            a[i]+=1
            x//=i
    if x>2:
        a[x]=1
    for i in a:
        prod*=(a[i]+1)
        prod%=mod
    return (prod//2)%mod

def buildSparseTable(n):
    global dp
    global p2
    global deptharr
    dp=[[-1 for i in range(18)] for j in range(n)]
    for i in range(1,n):
        dp[i-1][0]=i-1 if deptharr[i]>deptharr[i-1] else i
    for l in range(1,15):
        for i in range(n):
            if dp[i][l-1]!=-1 and dp[i+p2[l-1]][l-1]!=-1:
                dp[i][l]=dp[i+p2[l-1]][l-1] if (deptharr[dp[i][l-1]]>deptharr[dp[i+p2[l-1]][l-1]]) else dp[i][l-1]
            else:
                break
def query(l,r):
    global logn
    global p2
    d=r-l
    dx=logn[d]
    if l==r:
        return l
    if (deptharr[dp[l][dx]] > deptharr[dp[r-p2[dx]][dx]]): 
        return dp[r-p2[dx]][dx]
    else:
        return dp[l][dx]

def preprocess():
    global ptr
    global p2
    global logn
    p2[0]=1
    for i in range(1,18):
        p2[i]=p2[i-1]*2
    val=1
    ptr=0
    for i in range(1,maxi):
        logn[i]=ptr-1
        if val==i:
            val*=2
            logn[i]=ptr
            ptr+=1

def dfs(cur,prev,dep):
    global ptr
    if FAI[cur]==-1:
        FAI[cur]=ptr
    level[cur]=dep
    euler.append(cur)
    ptr+=1
    for i in adj[cur]:
        if i!=prev:
            dfs(i,cur,dep+1)
            euler.append(cur)
            ptr+=1

def makeArr():
    for i in euler:
        deptharr.append(level[i])

def LCA(u,v):
    if u==v:
        return u
    if FAI[u]>FAI[v]:
        (u,v)=(v,u)
    return euler[query(FAI[u],FAI[v])]

def addedge(a,b):
    adj[a].append(b)
    adj[b].append(a)

for _ in range(int(input())):
    n=int(input())
    parentage=[1]*(n+1)
    for j in range(n-1):
        a,b=map(int,input().split())
        addedge(a,b)
        parentage[max(a,b)]=min(a,b)
    preprocess()
    ptr=0
    dfs(1,0,0)
    makeArr()
    buildSparseTable(len(deptharr))
    costarray=[1]+list(map(int,input().split()))
    costmatrix=[1]*(n+1)
    parentage[1]=0
    for i in range(1,n+1):
        costmatrix[i]=costarray[i]*costmatrix[parentage[i]]
    print(costmatrix)
    for i in range(int(input())):
        a,b=map(int,input().split())
        j=LCA(a,b)
        print(j)
        print(costmatrix[a],costmatrix[b],costmatrix[j])
        prod=costmatrix[a]*costmatrix[b]*costarray[j]
        prod/=(costmatrix[j]*costmatrix[j])
        print(prod,findfactors(int(prod)))
