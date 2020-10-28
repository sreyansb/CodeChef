"""
10
6 3
1 2 3 3 2 1
20 2
1 2 3 4 5 6 7 8 9 10 2 2 13 14 15 16 4 4 4 4
6 2
1 2 3 4 1 2
4 1
7 6 7 6
"""

for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    visited=[0]*(n+1)
    visited[-2]=k#atleast one table toh lagegi hi=>last waale ko ek table dedo.
    for index in range(n-2,-1,-1):
        table=[0]*101#represents number of people in a table
        pro=1000000
        m=0
        for i in range(index,n):#the last index n-1 represents taking all things in one table
            #index n-i represents us taking i tables for the operation and related costs            
            if table[fams[i]]:
                if table[fams[i]]==1:
                    m+=2
                else:
                    m+=1
            table[fams[i]]+=1
            #print(index,i,visited[i+1])
            pro=min(pro,m+visited[i+1]+k)
        visited[index]=pro
    #print(visited)
    print(visited[0])
        
            

"""
#Accepted
import sys
sys.setrecursionlimit(10**6)
#runtime error because of recursion limit reached
def recur(index,fams,visited,n,k):
    #print(index,visited)
    if index>=n:
        return 0
    if visited[index]!=-1:
        return visited[index]
    table=[0]*105
    m=0
    totalhere=10000000
    try:
        for i in range(index,n):
            if table[fams[i]]:
                if table[fams[i]]==1:
                    m+=2
                else:
                    m+=1
            table[fams[i]]+=1
            g=recur(i+1,fams,visited,n,k)
            print(index,i,g)
            totalhere=min(totalhere,m+g+k)
    except Exception as e:
        pass
    visited[index]=totalhere
    return visited[index]
    
for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    visited=[-1]*n
    ans=recur(0,fams,visited,n,k)
    print(visited)
    print(ans)
"""
"""

#TLE
def recur(fams,ans,index,n,cost,visited,famtable,k,curtable):
    #print(index,cost)
    if index==n:
        ans.append(cost)
        return
    
    if visited[fams[index]]==0 or famtable[fams[index]]!=curtable:
        visited[fams[index]]=1
        famtable[fams[index]]=curtable
        recur(fams,ans,index+1,n,cost,visited,famtable,k,curtable)
        
    elif visited[fams[index]]==1:
        visited[fams[index]]=2
        famtable[fams[index]]=curtable
        recur(fams,ans,index+1,n,cost+2,visited,famtable,k,curtable)
        visited[fams[index]]=1
        famtable[fams[index]]=curtable+1
        recur(fams,ans,index+1,n,cost+k,visited,famtable,k,curtable+1)
        
    elif visited[fams[index]]>1 :
        visited[fams[index]]+=1
        famtable[fams[index]]=curtable
        recur(fams,ans,index+1,n,cost+1,visited,famtable,k,curtable)
        visited[fams[index]]=1
        famtable[fams[index]]=curtable+1
        recur(fams,ans,index+1,n,cost+k,visited,famtable,k,curtable+1) 

for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    cost=k
    table=1
    famtable=[0]*101
    numberintable=[0]*101
    for i in fams:
        if famtable[i]==0 or famtable[i]!=table:
            famtable[i]=table
            numberintable[i]=1
        else:
            if numberintable[i]==1:
                j=min(cost+k,cost+2)
            else:
                j=min(cost+k,cost+1)
            if j==cost+k :
                table+=1
                cost+=k
                famtable[i]=table
                numberintable[i]=1
            else:
                cost+=j-cost
                numberintable[i]+=1
        #print(i,cost)
    if k==1:
        print(cost)
    else:
        ans=[]
        recur(fams,ans,0,n,k,[0]*101,[0]*101,k,1)
        print(ans)
        print(min(ans))

        
"""
"""
#main attempt
for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    table=1
    famtable=[0]*101
    numberintable=[0]*101
    cost=k
    if k==2:
        i=0
        while i<n:
            if numberintable[i]==0 or famtable[i]!=table:
                famtable[i]=table
                
        print(cost)
    else:
        for i in fams:
            if famtable[i]==0 or famtable[i]!=table:
                famtable[i]=table
                numberintable[i]=1
            else:
                if numberintable[i]==1:
                    j=min(cost+k,cost+2)
                else:
                    j=min(cost+k,cost+1)
                if j==cost+k :
                    table+=1
                    cost+=k
                    famtable[i]=table
                    numberintable[i]=1
                else:
                    cost+=j-cost
                    numberintable[i]+=1
            #print(i,cost)
        print(cost)
"""

"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    table=1
    famtable=[0]*101
    numberintable=[0]*101
    cost=k
    for i in fams:
        if famtable[i]==0:
            famtable[i]=table
            numberintable[i]+=1
        elif famtable[i]!=table:
            famtable[i]=table
            numberintable[i]=1
        else:
            if numberintable[i]==1:
                j=min(cost+k,cost+2)
            else:
                j=min(cost+k,cost+1)
            if j==cost+k and j!=cost+numberintable[i]+1:
                table+=1
                cost+=k
                famtable[i]=table
                numberintable[i]=1
            else:
                cost+=j-cost
                numberintable[i]+=1
    print(cost)
"""                        

"""
#wrong judgment of problem
from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    fams=list(map(int,input().split()))
    counts=Counter(fams)
    sortcount=sorted(counts,key=lambda x:counts[x])
    init_ans=counts[sortcount[-1]]*k
    init_anstemp=counts[sortcount[-1]]*k
    init_value=counts[sortcount[-1]]
    i=1
    while(i<init_value):
        init_ans=min(init_ans,init_anstemp-k*i+i+1)
        i+=1
    print(init_ans)
"""
