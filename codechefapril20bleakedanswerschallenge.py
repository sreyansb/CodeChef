"""from random import randint
from random import seed
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    l=[]
    i=1
    for i in range(n):
        a=list(map(int,input().split()))
        seed()
        j=randint(1,max(k,224))
        l.append(a[j])
    print(*l)"""
"""
from random import randint
from random import seed
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    l=[]
    i=1
    for i in range(n):
        a=list(map(int,input().split()))
        seed()
        j=randint(1,max(k,224))
        j%=k
        l.append(a[j])
    print(*l)"""
from random import randint
from random import seed
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    l=[]
    i=1
    for i in range(n):
        a=list(map(int,input().split()))
        a.sort()
        di={}
        for i in a:
            if i not in di:
                di[i]=0
            di[i]+=1
        mini=min(di.keys(), key=(lambda k:di[k]))
        l.append(mini)
    print(*l)
"""
from random import randint
from random import seed
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    l=[]
    i=1
    for i in range(n):
        a=list(map(int,input().split()))
        seed()
        j=randint(0,50000)
        j&=k
        #print(j)
        j=1 if (j==0 or j==k)else j
        l.append(a[j])
    print(*l)
"""
"""
#0.747
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    l=[]
    j=k-1
    symbol='-'
    for i in range(n):
        a=list(map(int,input().split()))
        if j==0:
            symbol='+'
        if j==k-1:
            symbol='-'
        if symbol=='+':
            j+=1
            j%=k
        else:
            j-=1
            j%=k
        l.append(a[j])
    print(*l)
"""
"""
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    mini=0
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        k=set(a)
        tobefound=a[0]
        for i in k:
            if i!=tobefound:
                tobefound=i
                break
        if mini==0:
            l.append(tobefound)
            mini+=1
        else:
            l.append((tobefound+1)%m)
    print(*l)
"""
