import math
from collections import Counter

mod=1000000007
factors={}
factorlist=[]

def prepro():
    global factors
    global factorlist
    n=1000005
    prime=[True for i in range(0,n+1)]
    p=2
    s=set()
    while (p<=n):
        if prime[p]==True:
            factorlist.append(p)
            factors[p]=Counter({p:1})
            for i in range(2*p,n+1,p):
                prime[i]=False
        p+=1
    factors[1]=Counter({1:0})

def fillcostmatrix(costmatrix,cost,parentage,n,index=2):
    if index>n:
        return
    #print(index)
    #print(costmatrix[parentage[index]])
    if costmatrix[parentage[index]]:
        costmatrix[index]=factors[cost[index]]+costmatrix[parentage[index]]
        if costmatrix[index]:
            return fillcostmatrix(costmatrix,cost,parentage,n,index+1)
        else:
            costmatrix[index]=Counter({1:0})
            return fillcostmatrix(costmatrix,cost,parentage,n,index+1)
    else:
        return fillcostmatrix(costmatrix,cost,parentage,n,parentage[index])

def findfactors(i):
    global factors
    fac=Counter({})
    z=i
    if i in factors:
        return
    for k in factorlist:
        #print(i)
        if i==1:
            break
        while i%k==0:
            #print(i)
            if i==1:
                break
            fac+=factors[k]
            i//=k
    factors[z]=fac

def dfs(u,p,memo,lev,log,g):
    memo[u][0]=p
    for i in range(1,log+1):
        memo[u][i]=memo[memo[u][i - 1]][i - 1]
    for v in g[u]:
        if v!=p:
            lev[v]=lev[u]+1
            dfs(v, u, memo, lev, log, g)

def lca(u, v, log, lev, memo) :
    if (lev[u] < lev[v]):
        (u,v)=(v,u)
    for i in range(log,-1,-1): 
        if ((lev[u] - 2**i) >= lev[v]):
            u = memo[u][i] 
    if (u == v):
        return u
    for i in range(log,-1,-1):
        if memo[u][i]!=memo[v][i]:
            u=memo[u][i]
            v=memo[v][i]
    return memo[u][0]

t=int(input())
prepro()
for _ in range(t):
    
    n=int(input())
    g=[[] for i in range(n+1)]
    log=math.ceil(math.log2(n))
    memo=[[-1 for i in range(log+1)] for i in range(n+1)]
    lev=[0]*(n+1)
    parents=[]
    parentage=[0]*(n+1)
    for i in range(n-1):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
        parents.append((a,b))
    parents.sort(key=lambda x:x[0])
    for i in parents:
        parentage[i[1]]=i[0]
    print(parentage)
    #print("graph accepted")
    dfs(1,1,memo,lev,log,g)
    #print("dfs done")
    cost=[0]+list(map(int,input().split()))
    #print("cost accepted")
    q=int(input())
    queries=[]*q
    for i in range(q):
        a,b=map(int,input().split())
        queries.append((a,b))
    prepro()
    for i in cost[1:]:
        findfactors(i)
    costmatrix=[Counter({})]*(n+1)
    costmatrix[1]=factors[cost[1]]
    fillcostmatrix(costmatrix,cost,parentage,n)
    print(costmatrix)
    #queries.sort(key=lambda x:x[0])
    for i in queries:
        a,b=i[0],i[1]
        j=lca(a,b,log,lev,memo)
        #print(j)
        #print(costmatrix)
        prod=costmatrix[a]+costmatrix[b]+factors[cost[j]]+Counter({1:0})+Counter({1:0})
        prod=prod-costmatrix[j]-costmatrix[j]
        print(prod)
        prod1=1
        #print("a",costmatrix[a],"b",costmatrix[b])
        for i in dict(prod):
            prod1=((prod1%mod)*((prod[i]+1)%mod))%mod
        print(prod1)

"""
#ACCEPTED DFS
import math

mod=(10**9)+7

def calc(path,a):
    dic={}
    for i in range(len(path)):
        dic=primeFactors(a[path[i]-1],dic)
    value=list(dic.values())
    ans=1
    for i in range(len(value)):
        ans*=(value[i]+1)
        ans=ans%mod
    print(ans)
    
def primeFactors(n,dic):
    while n % 2 == 0:
        if 2 not in dic:
            dic[2]=1
        else:
            dic[2]+=1
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1 
            n = n / i
    if n > 2: 
        if n not in dic:
            dic[n]=1
        else:
            dic[n]+=1 
    return dic
    
def addEdge(x, y,v):
    v[x].append(y) 
    v[y].append(x)  
    
def DFS(vis, x, y, stack,v,ansflag,a):
    stack.append(x) 
    if (x == y):
        ansflag=1
        calc(stack,a)
        return 
    vis[x] = True
    flag = 0
    if (len(v[x]) > 0): 
        for j in v[x]: 
            if (vis[j] == False): 
                DFS(vis, j, y, stack,v,ansflag,a) 
                if(ansflag==1):
                    flag = 1  
                    break
      
    if (flag == 0): 
        del stack[-1] 
            
    return 

def DFSCall(x, y, n, stack,v,a):
    ansflag=0
    vis = [0 for i in range(n + 1)] 
    if(x!=y):
        x1=DFS(vis, x, y, stack,v,ansflag,a)
    else:
        x1=[x]
        calc(x1,a)
    return

for _ in range(int(input())):
    n = int(input())
    v = [[] for i in range(n+1)]
    for i in range(n-1):
        a1,b=map(int,input().split())
        addEdge(a1,b,v) 
    a=list(map(int,input().split()))
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        stack = []
        DFSCall(x,y,n,stack,v,a)
"""

"""mod=10**9+7
from collections import deque
from collections import Counter

def findfactors(x):
    prod=1
    a={1:0}
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
    return Counter(a)

def findprod(c):
    c=dict(c)
    prod=1
    for i in c:
        prod*=(c[i]+1)
        prod%=mod
    print(prod)

def bfs(n,graph,path,node=1):
    visited=[0]*(n+1)
    qu=deque()
    qu.append((node,-1))
    visited[node]=1
    while(len(qu)):
        #print(path)
        j=qu[0]
        qu.popleft()
        visited[j[0]]=1
        for i in graph[j[0]]:
            if visited[i]==0:
                qu.append((i,j[0]))
                path[i]=path[j[0]].copy()
                path[i].append(j[0])
                #print(path)

def happyq(node1,node2,cost,path,z):
    prod=Counter({})
    ans1=path[node1]
    ans2=path[node2]
    ans1.append(node1)
    ans2.append(node2)
    #print(ans1)
    if node1==node2:
        findprod(z[node1])
    else:
        cnt=0
        j=len(ans1)-len(ans2)
        if j>0:
            anstemp=ans1.copy()
            ans1=ans2.copy()
            ans2=anstemp.copy()
            
        for i in range(len(ans1)-1,-1,-1):
            cnt=i
            prod=(prod + z[ans1[i]])
            if ans1[i]==ans2[i]:
                break
            #print(prod)
        for i in range(cnt+1,len(ans2)):
            prod=(prod + z[ans2[i]])
        findprod(prod)
        
for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    path=[[] for i in range(n+1)]
    #print(path)
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    cost=[0]+list(map(int,input().split()))
    z=[0]+list(map(findfactors,cost[1:]))
    #print(z)
    bfs(n,graph,path)
    #print(path)
    for _2 in range(int(input())):
        l,r=map(int,input().split())
        happyq(l,r,cost,path,z)
"""
"""
mod=1000000007

def SieveOfEratosthenes(n, prime,primesquare, a):  
    for i in range(2,n+1): 
        prime[i] = True
        
    for i in range((n * n + 1)+1): 
        primesquare[i] = False
   
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
    
        if (prime[p] == True): 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
  
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            
            a[j] = p 
  
            primesquare[p * p] = True
            j+=1
  
def findfactors(n): 
    if (n == 1): 
        return 1
  
    prime = [False]*(n + 2) 
    primesquare = [False]*(n * n + 2) 
      
    a = [0]*(n +2)
  
    SieveOfEratosthenes(n, prime, primesquare, a) 
   
    ans = 1

    i=0
    while(1):  
        if(a[i] * a[i] * a[i] > n): 
            break
  
        # Calculating power of a[i] in n. 
        cnt = 1 # cnt is power of  
                # prime a[i] in n. 
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            cnt = cnt + 1 # incrementing power 
  
        ans = ans * cnt 
        i+=1

      
    n=int(n) 
    # First case 
    if (prime[n]==True): 
        ans = ans * 2
  
    # Second case 
    elif (primesquare[n]==True): 
        ans = ans * 3
  
    # Third casse 
    elif (n != 1): 
        ans = ans * 4
  
    return ans%mod

def dfss(graph,visited,start,end,stack):
    try:
        
        stack.append(start)
        if start==end:
            return stack
        visited[start]=1
        flag=0
        if (graph[start]):
            for i in graph[start]:
                if visited[i]==0:
                    dfss(graph,visited,i,end,stack)
                    flag=1
        if flag==0:
            stack.pop()
    except:
        print("dfss")

def bfs(graph, start, end,stack):
    vis=[0]*(n+1)
    dfss(graph,vis,start,end,stack)
    

for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    for _1 in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    costarray=[0]+list(map(int,input().split()))
    #result=parse(1,graph)
    #print(result)
    for _2 in range(int(input())):
        a,b=map(int,input().split())
        stack=[]
        bfs(graph,a,b,stack)
        #print(stack)
        prod=1
        #print(stack)
        for i in stack:
            #print("i",i)
            prod*=costarray[i]
        print(findfactors(prod))"""
"""
import sys
sys.setrecursionlimit(10**8)
mod=1000000007

def findfactors(n):
    cnt=1 if n==1 else 2
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            cnt+=1 if n//i==i else 2 
    return cnt%mod
    
def dfs(graph,visited,start_vertex,end_vertex,stack):
    #print(start_vertex)
    stack.append(start_vertex)
    #print(start_vertex)
    #cost*=costarray[start_vertex]
    if start_vertex==end_vertex:
        return
    #print(stack)
    visited[start_vertex]=1
    flag=0
    if len(graph[start_vertex]):
        k=len(stack)
        for j in graph[start_vertex]:
            if visited[j]==0:           
                dfs(graph,visited,j,end_vertex,stack)
                if len(stack)!=k:
                    flag=1
    if flag==0:
        stack.pop()
    

for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    for _1 in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    costarray=[0]+list(map(int,input().split()))
    #result=parse(1,graph)
    #print(result)
    for _2 in range(int(input())):
        a,b=map(int,input().split())
        visited=[0]*(n+1)
        stack=[]
        dfs(graph,visited,a,b,stack)
        #print(stack)
        prod=1
        #print(stack)
        for i in stack:
            #print("i",i)
            prod*=costarray[i]
        print(findfactors(prod))"""
"""
mod=1000000007

def findfactors(n):
    cnt=1 if n==1 else 2
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            cnt+=1 if n//i==i else 2 
    return cnt%mod
    
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph[node]:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    

for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    for _1 in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    costarray=[0]+list(map(int,input().split()))
    #result=parse(1,graph)
    #print(result)
    for _2 in range(int(input())):
        a,b=map(int,input().split())
        stack=bfs(graph,a,b)
        #print(stack)
        prod=1
        #print(stack)
        for i in stack:
            #print("i",i)
            prod*=costarray[i]
        print(findfactors(prod))"""

"""
def SieveOfEratosthenes(n, prime,primesquare, a):  
    for i in range(2,n+1): 
        prime[i] = True
        
    for i in range((n * n + 1)+1): 
        primesquare[i] = False
   
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
    
        if (prime[p] == True): 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
  
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            
            a[j] = p 
  
            primesquare[p * p] = True
            j+=1
  
def findfactors(n): 
    if (n == 1): 
        return 1
  
    prime = [False]*(n + 2) 
    primesquare = [False]*(n * n + 2) 
      
    a = [0]*(n +2)
  
    SieveOfEratosthenes(n, prime, primesquare, a) 
   
    ans = 1

    i=0
    while(1):  
        if(a[i] * a[i] * a[i] > n): 
            break
  
        # Calculating power of a[i] in n. 
        cnt = 1 # cnt is power of  
                # prime a[i] in n. 
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            cnt = cnt + 1 # incrementing power 
  
        ans = ans * cnt 
        i+=1

      
    n=int(n) 
    # First case 
    if (prime[n]==True): 
        ans = ans * 2
  
    # Second case 
    elif (primesquare[n]==True): 
        ans = ans * 3
  
    # Third casse 
    elif (n != 1): 
        ans = ans * 4
  
    return ans%mod
"""


"""
mod=10**9+7
from collections import deque
from collections import Counter 
def SieveOfEratosthenes(n, prime,primesquare, a):  
    for i in range(2,n+1): 
        prime[i] = True
        
    for i in range((n * n + 1)+1): 
        primesquare[i] = False
   
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
    
        if (prime[p] == True): 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
  
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            
            a[j] = p 
  
            primesquare[p * p] = True
            j+=1
  
def countDivisors(n): 
    if (n == 1): 
        return 1
  
    prime = [False]*(n + 2) 
    primesquare = [False]*(n * n + 2) 
      
    a = [0]*n 
  
    SieveOfEratosthenes(n, prime, primesquare, a) 
   
    ans = 1

    i=0
    while(1):  
        if(a[i] * a[i] * a[i] > n): 
            break
  
        # Calculating power of a[i] in n. 
        cnt = 1 # cnt is power of  
                # prime a[i] in n. 
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            cnt = cnt + 1 # incrementing power 
  
        # Calculating number of divisors 
        # If n = a^p * b^q then total  
        # divisors of n are (p+1)*(q+1) 
        ans = ans * cnt 
        i+=1
  
    # if a[i] is greater than 
    # cube root of n 
      
    n=int(n) 
    # First case 
    if (prime[n]==True): 
        ans = ans * 2
  
    # Second case 
    elif (primesquare[n]==True): 
        ans = ans * 3
  
    # Third casse 
    elif (n != 1): 
        ans = ans * 4
  
    return ans%mod

def bfs(n,graph,path,node=1):
    visited=[0]*(n+1)
    qu=deque()
    qu.append((node,-1))
    visited[node]=1
    while(len(qu)):
        #print(path)
        j=qu[0]
        qu.popleft()
        visited[j[0]]=1
        for i in graph[j[0]]:
            if visited[i]==0:
                qu.append((i,j[0]))
                path[i]=path[j[0]].copy()
                path[i].append(j[0])
                #print(path)

def happyq(node1,node2,cost,path):
    prod=1
    ans1=path[node1].copy()
    ans2=path[node2].copy()
    ans1.append(node1)
    ans2.append(node2)
    #print(ans1)
    if node1==node2:
        print(countDivisors(cost[node1]))
    else:
        cnt=0
        j=len(ans1)-len(ans2)
        if j>0:
            anstemp=ans1.copy()
            ans1=ans2.copy()
            ans2=anstemp.copy()
        prod =1
        for i in range(len(ans1)-1,-1,-1):
            cnt=i
            prod=(prod * cost[ans1[i]])
            if ans1[i]==ans2[i]:
                break
            #print(ans1[i],prod)
        #print(ans2,cnt)
        for i in range(cnt+1,len(ans2)):
            prod=(prod * cost[ans2[i]])
            #print(ans2[i],prod)
            
        print(countDivisors(prod))
        
        
for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    path=[[] for i in range(n+1)]
    #print(path)
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    cost=[0]+list(map(int,input().split()))
    #print(z)
    bfs(n,graph,path)
    #print(path)
    for _2 in range(int(input())):
        l,r=map(int,input().split())
        happyq(l,r,cost,path)
"""
"""mod=10**9+7
from collections import deque
from collections import Counter 
def findfactors(x):
    prod=1
    a={1:0}
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
    return Counter(a)

def findprod(c):
    c=dict(c)
    prod=1
    for i in c:
        prod*=(c[i]+1)
        prod%=mod
    print(prod)

def bfs(n,graph,path,node=1):
    visited=[0]*(n+1)
    qu=deque()
    qu.append((node,-1))
    visited[node]=1
    while(len(qu)):
        #print(path)
        j=qu[0]
        qu.popleft()
        visited[j[0]]=1
        for i in graph[j[0]]:
            if visited[i]==0:
                qu.append((i,j[0]))
                path[i]=path[j[0]].copy()
                path[i].append(j[0])
                #print(path)

def happyq(node1,node2,cost,path,z):
    prod=Counter({})
    ans1=path[node1]
    ans2=path[node2]
    ans1.append(node1)
    ans2.append(node2)
    #print(ans1)
    if node1==node2:
        findprod(z[node1])
    else:
        cnt=0
        j=len(ans1)-len(ans2)
        if j>0:
            anstemp=ans1.copy()
            ans1=ans2.copy()
            ans2=anstemp.copy()
            
        for i in range(len(ans1)-1,-1,-1):
            cnt=i
            prod=(prod + z[ans1[i]])
            if ans1[i]==ans2[i]:
                break
            #print(prod)
        for i in range(cnt+1,len(ans2)):
            prod=(prod + z[ans2[i]])
        findprod(prod)
        
for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    path=[[] for i in range(n+1)]
    #print(path)
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    cost=[0]+list(map(int,input().split()))
    z=[0]+list(map(findfactors,cost[1:]))
    #print(z)
    bfs(n,graph,path)
    #print(path)
    for _2 in range(int(input())):
        l,r=map(int,input().split())
        happyq(l,r,cost,path,z)
"""   

"""
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

def dfs(graph,visited,start_vertex,end_vertex,stack):
    #print(start_vertex)
    stack.append(start_vertex)
    #print(start_vertex)
    #cost*=costarray[start_vertex]
    if start_vertex==end_vertex:
        return 
    visited[start_vertex]=1
    flag=0
    if len(graph[start_vertex]):
        for j in graph[start_vertex]:
            if visited[j]==0:           
                dfs(graph,visited,j,end_vertex,stack)
                flag=1
    if flag==0:
        stack.pop()

for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    for _1 in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    costarray=[0]+list(map(int,input().split()))
    #result=parse(1,graph)
    #print(result)
    for _2 in range(int(input())):
        a,b=map(int,input().split())
        visited=[0]*(n+1)
        stack=[]
        dfs(graph,visited,a,b,stack)
        #print(stack)
        prod=1
        for i in stack:
            prod*=costarray[i]
        print(findfactors(prod))
"""
"""
block_sz=0
parent=[0]*(100001)
depth=[0]*(100001)
jump_parent=[0]*(100001)
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

def findheight(i,graph,visited):
    if visited[i]:
        return 0
    visited[i]=1
    height=1
    #print(i)
    for j in graph[i]:
        height=max(height,1+findheight(j,graph,visited))
    return height

def LCAnaive(u,v,cost,cost_matrix):
    cost[0]*=cost_matrix[u]
    if u==v:
        return u
    if depth(u)>depth(v):
        (u,v)=(v,u)
    v=parent[v]
    return LCAnaive(u,v,cost)

def lcasqrt(graph,u,v,c,cost_matrix):
    while(jump_parent[u]!=jump_parent[v]):
        if depth[u]>depth[v]:
            (u,v)=(v,u)
        v=jump_parent[v]
    return LCAnaive(u,v,c,cost_matrix)

def dfs(graph,child,parenty):
    depth[child]=depth[parenty]+1
    parent[child]=parenty
    if depth[child]%block_sz==0:
        jump_parent[child]=parent[child]
    else:
        jump_parent[child]=jump_parent[parenty]
    if len(graph[child]):
        for i in graph[child]:
            if i!=parenty:
                dfs(graph,i,child)

for _ in range(int(input())):
    n=int(input())
    graph=[[] for i in range(n+1)]
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[0]*(n+1)
    cost_matrix=list(map(int,input().split()))
    height=findheight(1,graph,visited)
    block_sz=int(height**0.5)
    depth[0]=-1
    dfs(graph,1,0)
    for _2 in range(int(input())):
        a,b=map(int,input().split())
        c=[1]
        lcasqrt(graph,a,b,c,cost_matrix)
        print(c[0])
        print(findfactors(c[0]))
"""      
"""
#import math
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
    parentage=[0]*(n+1)
    parentage[1]=1
    for _1 in range(n-1):
        a,b=sorted(list(map(int,input().split())))
        parentage[b]=a        
    costarray=[0]+list(map(int,input().split()))
    print(costarray)
    #result=parse(1,graph)
    #print(result)
    for _2 in range(int(input())):
        a,b=sorted(list(map(int,input().split())))
        prod=1
        while(b!=a):
            prod*=costarray[b]
            b=parentage[b]
        prod*=costarray[a]
        print(findfactors(prod))
"""
"""
def parse(node, tree, depth=1):
    result = []
    if node not in tree:
        return [[node] * depth]
    else:
        res = []
        for next_node in tree[node]:
            res.extend(parse(next_node, tree, depth+1))
        for r in res:
           r[depth-1] = node
           result.append(r)
        return result
"""
