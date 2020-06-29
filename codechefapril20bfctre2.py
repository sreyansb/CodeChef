#block_sz=0
#parent=[0]*(100001)
#depth=[0]*(100001)
#jump_parent=[0]*(100001)
mod=10**9+7

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

for _ in range(int(input())):
    n=int(input())
    parentage=[1]*(n+1)
    graph=[[] for i in range(n+1)]
    newparentage=[[] for i in range(n+1)]
    for _1 in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        parentage[max(a,b)]=min(a,b)
        
    newparentage[1]=[1]
    costarray=[0]+list(map(int,input().split()))
    costmatrix=[1]*(n+1)
    costmatrix[1]=costarray[1]
    
    for i in range(2,n+1):
        costmatrix[i]=costarray[i]*costmatrix[parentage[i]]
        newparentage[i]=newparentage[parentage[i]]+[i]

    for _2 in range(int(input())):
        a,b=map(int,input().split())
        #j=lcasqrt(graph,a,b)
        k=max(set(newparentage[a])&set(newparentage[b]))
        #print(k)
        prod=costmatrix[a]*costmatrix[b]*costarray[k]
        prod/=(costmatrix[k]*costmatrix[k])        
        #prod=(costmatrix[a]*costmatrix[b])*costarray[j]
        #prod/=(costmatrix[j]*costmatrix[j])
        print(findfactors(int(prod)))
"""
def findheight(i,graph,visited):
    if visited[i]:
        return 0
    height=1
    visited[i]=1
    #print(i)
    for j in graph[i]:
        height=max(height,1+findheight(j,graph,visited))
    return height

def LCAnaive(u,v):
    if u==v:
        return u
    if depth[u]>depth[v]:
        (u,v)=(v,u)
    v=parent[v]
    return LCAnaive(u,v)

def lcasqrt(graph,u,v):
    while(jump_parent[u]!=jump_parent[v]):
        if depth[u]>depth[v]:
            (u,v)=(v,u)
        v=jump_parent[v]
    return LCAnaive(u,v)

def dfs(graph,child,parenty):
    depth[child]=depth[parenty]+1
    parent[child]=parenty
    if depth[child]%block_sz==0:
        jump_parent[child]=parent[child]
    else:
        jump_parent[child]=jump_parent[parenty]
    for i in range(len(graph[child])):
            if graph[child][i]!=parenty:
                dfs(graph,graph[child][i],child)"""
"""
    visited=[0]*(n+1)
    height=findheight(1,graph,visited)
    block_sz=int(height**0.5)
    depth[0]=-1
    dfs(graph,1,0)
    
    
    costmatrix=[1]*(n+1)
    costmatrix[1]=costarray[1]
    for i in range(2,n+1):
        costmatrix[i]=costarray[i]*costmatrix[parentage[i]]
    """                                      
