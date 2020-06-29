def issort(a,m):
    counts=0
    i=0
    while(i<len(a)):
        #print(a)
        if a[i]==i+1:
            i+=1
        else:
            a[i],a[a[i]-1]=a[a[i]-1],a[i]
            if (i,a[i]-1) in m:
                pass
            else:
                counts+=1
            i+=1
    print(a)
    return(counts)

for _ in range(int(input())):
    n,mi=map(int,input().split())
    a=list(map(int,input().split()))
    m=[]
    for i in range(mi):
        j,b=map(int,input().split())
        m.append((j-1,b-1))
        m.append((b-1,j-1))
    print(issort(a,m))

"""
def fillispath(parent,src,k,ispath):
    while src!=k and parent[k]!=-1:
        ispath[src][k]=1
        ispath[k][src]=1
        k=parent[k]
        #print(k,src)
    #print(ispath)
    
def performbfs(adjList, src, n,ispath):  
    parent = [-1] * (n)  
    que = [0] * (n)  
    front, rear = -1, -1
    visited = [0] * (n)  
    visited[src] = 1
    parent[src] = 1  
    rear += 1
    que[rear] = src  
    while front != rear:  
        front += 1
        k = que[front]  
        List = adjList[k]  
        for i in range(0, len(List)):  
            j = List[i] 
            if visited[j] == 0: 
                rear += 1
                que[rear] = j  
                visited[j] = 1
                parent[j] = k
    #print(src,parent)
    for k in range(n):
        fillispath(parent,src,k,ispath)
        
def minSwaps1(arr,m,ispath): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1])
    #print(arrpos)
    vis = {k:False for k in range(n)} 
    ans = 0
    allpaths=[]
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i
        
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            #print(i,j)
            cycle_size += 1
            if ispath[i][j] or ispath[j][i]:
                cycle_size-=1
            else:
             allpaths.append((i,j))
            #print(cycle_size,"ccc")
        if cycle_size > 0: 
            ans += (cycle_size - 1)
    print(allpaths)
    return ans

for _ in range(int(input())):
    n,mi=map(int,input().split())
    a=list(map(int,input().split()))
    m=[[] for i in range(n)]
    #print(m)
    for i in range(mi):
        j,b=map(int,input().split())
        m[j-1].append(b-1)
        m[b-1].append(j-1)
    #print(m)
    ispath=[[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        performbfs(m,i,n,ispath)
    #print(ispath)
    print(minSwaps1(a,m,ispath))
"""          
                
        
