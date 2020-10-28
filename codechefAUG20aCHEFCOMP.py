import sys
sys.setrecursionlimit(10**6)
for _ in range(int(input())):
    n=int(input())
    graph=[[] for j in range(n+1)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    p=[0]+list(map(int,input().split()))
    a=[0]+list(map(int,input().split()))
    b=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)
    ans=[-1]*(n+1)
    def graphi(vertex,parent,value,day):
        if value>=b[vertex] and b[vertex]:
            b[vertex]=0
            ans[vertex]=day
        elif b[vertex]>value and b[vertex]:
            b[vertex]-=value
        #print(a,b)
        for i in graph[vertex]:
            if not(visited[i]) and i!=parent:
                graphi(i,vertex,value,day)
    for i in range(1,n+1):
        graphi(p[i],-1,a[p[i]],i)
        visited[p[i]]=1
    print(*ans[1:])
            
        
    
    
