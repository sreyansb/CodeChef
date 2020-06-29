for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
        if positions[i]!=i:
            incorrectpos.add(i)
    head=1
    sortarr=sorted(values)
    solutions=[]
    l=0
    while(head<=n and l<=k):
        #print(values[1:])
        if values[head]==head:
            incorrectpos-={head}
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            '''if valueatposition1==position1:
                solutions=[]
                l=0
                break'''
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if position1==values[position1]:
                    incorrectpos-={position1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                l+=1
            else:
                head+=1
    #print(head)
    #print()
    #print(values)
    #print()
    head=1
    while(head<=n and l<=k):
        #print(incorrectpos)
        if values[head]==head:
            incorrectpos-={head}
            head+=1
            continue
        else:
            pos1=values[head]
            position2=head
            for i in sorted(incorrectpos,reverse=True):
                if i!=head and i!=pos1 and values[i]!=values[values[i]]:
                    #print("i",i)
                    position2=i
                    break
            #print(position2)
            if position2==head:
                #print(head)
                l=0
                break
            else:
                #print(head,pos1,position2)
                values[head],values[pos1],values[position2]=values[position2],values[head],values[pos1]
                solutions.append([head,pos1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if pos1==values[pos1]:
                    incorrectpos-={pos1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                #print(values[1:])
                l+=1
    #print(l,values)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
    head=1
    sortarr=sorted(values)
    solutions=[]
    numbs=0
    l=0
    flaggy=1
    while(head<=n and l<=k):
        if values[head]==head:
            positions[head]=head
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    positions[head]=head
                    numbs+=1
                if position1==values[position1]:
                    positions[position1]=position1
                    numbs+=1
                if position2==values[position2]:
                    positions[position2]=position2
                    numbs+=1
                l+=1
            else:
                position2=head
                pos1=position1
                for i in range(n,head,-1):
                    if i!=positions[i] and i!=head and i!=pos1:
                        #print("i",i)
                        position2=i
                        break
                #print(position2)
                if position2==head:
                    #print(head)
                    flaggy=0
                    l=0
                    break
                else:
                    values[head],values[pos1],values[position2]=values[position2],values[head],values[pos1]
                    solutions.append([head,pos1,position2])
                    if head==values[head]:
                        positions[head]=head
                        numbs+=1
                    if position1==values[position1]:
                        positions[position1]=position1
                        numbs+=1
                    if position2==values[position2]:
                        positions[position2]=position2
                        numbs+=1
                    l+=1
    #print(values)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""
"""for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
    head=1
    sortarr=sorted(values)
    solutions=[]
    numbs=0
    l=0
    flaggy=1
    while(head<=n and l<=k):
        if values[head]==head:
            positions[head]=head
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    positions[head]=head
                    numbs+=1
                if position1==values[position1]:
                    positions[position1]=position1
                    numbs+=1
                if position2==values[position2]:
                    positions[position2]=position2
                    numbs+=1
                l+=1
            else:
                position2=head
                pos1=position1
                for i in range(n,0,-1):
                    if i!=positions[i] and i!=head and i!=pos1:
                        #print("i",i)
                        position2=i
                        break
                #print(position2)
                if position2==head:
                    #print(head)
                    flaggy=0
                    l=0
                    break
                else:
                    values[head],values[pos1],values[position2]=values[position2],values[head],values[pos1]
                    solutions.append([head,pos1,position2])
                    if head==values[head]:
                        positions[head]=head
                        numbs+=1
                    if position1==values[position1]:
                        positions[position1]=position1
                        numbs+=1
                    if position2==values[position2]:
                        positions[position2]=position2
                        numbs+=1
                    l+=1
    print(values)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""
"""
#Set difference-my approach.instead use hashing like in previous method.
#is slow, not accepted-TLE
for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
        if positions[i]!=i:
            incorrectpos.add(i)
    head=1
    sortarr=sorted(values)
    solutions=[]
    l=0
    while(head<=n and l<=k):
        #print(values[1:])
        if values[head]==head:
            incorrectpos-={head}
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if position1==values[position1]:
                    incorrectpos-={position1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                l+=1
            else:
                pos1=values[head]
                position2=head
                for i in incorrectpos:
                    if i!=head and i!=pos1:
                        #print("i",i)
                        position2=i
                        
                #print(position2)
                if position2==head:
                    #print(head)
                    l=0
                    break
                else:
                    #print(head,pos1,position2)
                    values[head],values[pos1],values[position2]=values[position2],values[head],values[pos1]
                    solutions.append([head,pos1,position2])
                    if head==values[head]:
                        incorrectpos-={head}
                    if pos1==values[pos1]:
                        incorrectpos-={pos1}
                    if position2==values[position2]:
                        incorrectpos-={position2}
                    #print(values[1:])
                    l+=1
    #print(l,values)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""
"""
def check(pos,values):
    pos1=values[pos]
    if pos1==values[pos1]:
        return 0
    pos2=values[pos1]
    if pos2!=values[pos2]:
        return 1
    else:
        return check(pos2,values)
for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
        if positions[i]!=i:
            incorrectpos.add(i)
    head=1
    sortarr=sorted(values)
    solutions=[]
    l=0
    while(head<=n and l<=k):
        #print(values)
        if values[head]==head:
            incorrectpos-={head}
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            if valueatposition1==position1:
                solutions=[]
                l=0
                break
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if position1==values[position1]:
                    incorrectpos-={position1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                l+=1
            else:
                position2=head
                for i in incorrectpos:
                    if i!=head and i!=position1 and check(i,values):
                        position2=i
                if position2==head:
                    solutions=[]
                    l=0
                    break
                else:
                    values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                    solutions.append([head,position1,position2])
                    if head==values[head]:
                        incorrectpos-={head}
                    if position1==values[position1]:
                        incorrectpos-={position1}
                    if position2==values[position2]:
                        incorrectpos-={position2}
                    l+=1
    #print(incorrectpos)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""
"""def check(pos,values):
    pos1=values[pos]
    if pos1==values[pos1]:
        return 0
    pos2=values[pos1]
    if pos2!=values[pos2]:
        return 1
    else:
        return check(pos2,values)
for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    incorrectpos=set()
    positions=[-1]*(n+1)
    for i in range(1,n+1):
        positions[values[i]]=i
        if positions[i]!=i:
            incorrectpos.add(i)
    head=1
    sortarr=sorted(values)
    solutions=[]
    l=0
    while(head<=n and l<=k):
        #print(values)
        if values[head]==head:
            incorrectpos-={head}
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            if valueatposition1==position1:
                solutions=[]
                l=0
                break
            
            position2=valueatposition1
            if position2!=head:
                #position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if position1==values[position1]:
                    incorrectpos-={position1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                l+=1
            else:
                position2=head
                for i in incorrectpos:
                    if i!=head and i!=position1 :#and check(i,values):
                        position2=i
                        
                if position2==head:
                    l=0
                    break
                else:
                    values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                    solutions.append([head,position1,position2])
                    if head==values[head]:
                        incorrectpos-={head}
                    if position1==values[position1]:
                        incorrectpos-={position1}
                    if position2==values[position2]:
                        incorrectpos-={position2}
                    l+=1
    #print(incorrectpos)
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
        else:
         print(-1)

"""
"""
import random
import time
a=list(range(1,100000))
random.shuffle(a)
n=len(a)
k=n//2
values=[0]+a
head=1
l=0
sortarr=sorted(values)
solutions=[]
print("started")
incorrectpos=set()
positions=[-1]*(n+1)
for i in range(1,n+1):
    positions[values[i]]=i
    if positions[i]!=i:
        incorrectpos.add(i)
head=1
sortarr=sorted(values)
solutions=[]
l=0
while(head<=n and l<=k):
    #print(values)
    if values[head]==head:
        incorrectpos-={head}
        head+=1
        continue
    else:
        position1=values[head]
        valueatposition1=values[position1]
        if valueatposition1==position1:
            solutions=[]
            l=0
            break
        position2=valueatposition1
        if position2!=head:
            position2=valueatposition1
            valueatposition2=values[position2]
            values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
            solutions.append([head,position1,position2])
            if head==values[head]:
                incorrectpos-={head}
            if position1==values[position1]:
                incorrectpos-={position1}
            if position2==values[position2]:
                incorrectpos-={position2}
            l+=1
        else:
            position2=head
            for i in incorrectpos:
                if i!=head and i!=position1:
                    position2=i
            if position2==head:
                solutions=[]
                l=0
                break
            else:
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                if head==values[head]:
                    incorrectpos-={head}
                if position1==values[position1]:
                    incorrectpos-={position1}
                if position2==values[position2]:
                    incorrectpos-={position2}
                l+=1
        
if l<=k and l>0:
    print("l")
    print("here1")
    print(l)
    for i in solutions:
        print(*i) 
else:
    if values==sortarr:
        #print(values)
        print("l")
        print("here2")
        print(0)
        print(*values)
        
        print()
    else:
     print(-1)

"""
"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    values=[0]+list(map(int,input().split()))
    head=1
    sortarr=sorted(values)
    solutions=[]
    l=0
    while(head<=n and l<=k):
        print(values)
        if values[head]==head:
            head+=1
            continue
        else:
            position1=values[head]
            valueatposition1=values[position1]
            if valueatposition1==position1:
                solutions=[]
                l=0
                break
            position2=valueatposition1
            if position2!=head:
                position2=valueatposition1
                valueatposition2=values[position2]
                values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                solutions.append([head,position1,position2])
                l+=1
            else:
                position2=head+1
                while(position2!=head):
                    if  position2==position1 or values[position2]==position2:
                        position2=((position2)%n)+1
                    else:
                        break
                if position2==head:
                    solutions=[]
                    l=0
                    break
                else:
                    values[head],values[position1],values[position2]=values[position2],values[head],values[position1]
                    solutions.append([head,position1,position2])
                    l+=1
    if l<=k and l>0:
        print(l)
        for i in solutions:
            print(*i) 
    else:
        if values==sortarr:
            print(0)
            print()
        else:
         print(-1)
"""

"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=0
    l=0
    v1=0
    mat=[]
    while(m<n):
        if a[m]!=m+1:
            if (a[a[m]-1]-1)!=m:
                mat.append([m+1,a[m],a[a[m]-1]])
                v=a[a[m]-1]
                a[a[m]-1]=a[m]
                a[m]=a[v-1]
                a[v-1]=v
                l+=1
            else:
                p=m+1
                while(p<n and(a[p]-1==p or p==a[m]-1)):
                      p+=1
                if p==n:
                      v1=1
                      break
                if [m+1,a[m],p+1] in mat:
                    v1=1
                    break
                mat.append([m+1,a[m],p+1])
                v=a[a[m]-1]
                a[a[m]-1]=a[m]
                a[m]=a[p]
                a[p]=v
                l+=1
        else:
            m+=1
    if v1:
        print(-1)
    else:
        print(l)
        for i in mat:
            print(*i)
"""
