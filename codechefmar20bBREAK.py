#ACCEPTED
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            a1=set(a)
            b1=set(b)
            if len(a1-b1)!=1:
                print("NO")
            else:
                a.sort()
                b.sort()
                flag=0
                for i in range(n):
                    if a[i]>=b[i]:
                        flag=1
                        break
                if not(flag):
                    print("YES")
                else:
                    print("NO")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a1=set(a)
        b1=set(b)
        k=a1-b1
        g=len(k)
        if g>=1:
            print("YES")
        else:
            flag=1
            for i in range(n):
                if a[i]>=b[i]:
                    flag=0
                    break
            if flag:
                print("YES")
            else:
                print("NO")
            
            
            
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            di={}
            #already tried removing the sort part.No help.
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                di[a[i]]=0
            for i in range(n):
                #has to be '>=' otherwise only 4 test cases passing.
                if a[i]>=b[i]:
                    flag=1
                    break
                di[a[i]]+=1#dont remove this line
                if b[i] in di:
                    di[b[i]]+=1
            pos=0#no use of removing pos
            if flag==0:
                for i in di:
                    if di[i]<2 and pos!=0:
                        flag=1
                    elif di[i]==1 and pos==0:
                        pos+=1
                    elif (di[i]==1 and pos==1):
                        flag=1
            if flag>0:
                print("NO")
            else:
                print("YES")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)==sum(b):
            print("NO")
        else:
            
            print("YES")

"""
"""t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                if a[i]>=b[i]:
                    print("NO")
                    flag=1
                    break
            if not(flag):
                print("YES")
"""
"""
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            di={}
            #already tried removing the sort part.No help.
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                if a[i]>=b[i]:
                    flag=1
                    break
            if flag>0:
                print("NO")
            else:
                print("YES")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)==sum(b):
            print("NO")
        else:
            
            print("YES")
"""

"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            di={}
            #already tried removing the sort part.No help.
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                if a[i]>=b[i]:
                    flag=1
                    break
            if flag>0:
                print("NO")
            else:
                print("YES")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)<=sum(b):
            print("NO")
        else:
            
            print("YES")
"""
"""t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            di={}
            #already tried removing the sort part.No help.
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                di[a[i]]=0
            for i in range(n):
                #has to be '>=' otherwise only 4 test cases passing.
                if a[i]>=b[i]:
                    flag=1
                    break
                di[a[i]]+=1
                if b[i] in di:
                    di[b[i]]+=1
            pos=0#no use of removing pos
            if flag==0:
                for i in di:
                    if di[i]<2 and pos!=0:
                        flag=1
                    elif di[i]==1 and pos==0:
                        pos+=1
                    elif (di[i]==1 and pos==1):
                        flag=1
            if flag>0:
                print("NO")
            else:
                print("YES")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)<=sum(b):
            print("NO")
        else:
            
            print("YES")
"""
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            k=len(set(a)&set(b))
            l=len(set(a)|set(b))
            if l+k<2*n:
                a.sort()
                b.sort()
                flag=0
                for i in range(n):
                    if a[i]>=b[i]:
                        flag=1
                        break
                if not(flag):
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)==sum(b):
            print("NO")
        else:
            print("YES")
"""
"""t,s=map(int,input().split())
if s==1:
    for _ in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            di={}
            #already tried removing the sort part.No help.
            a.sort()
            b.sort()
            flag=0
            for i in range(n):
                di[a[i]]=0
            for i in range(n):
                #has to be '>=' otherwise only 4 test cases passing.
                if a[i]>=b[i]:
                    flag=1
                    break
                di[a[i]]+=1        
                if b[i] in di:
                    di[b[i]]+=1
            pos=0#no use of removing pos
            if flag==0:
                for i in di:
                    if di[i]<2 and pos!=0:
                        flag=1
                        break
                    pos+=1
            if flag>0:
                print("NO")
            else:
                print("YES")
else:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if sum(a)==sum(b):
            print("NO")
        else:
            print("YES")
"""        
"""t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        l=a+b
        flag=1
        for i in range(1,n):
            if l[i:].count(l[i])<2:
                flag=0
                break
        for i in range(n):
            if a[i]>=b[i]:
                flag=0
                break
        if flag==0:
            print("NO")
        else:
            print("YES")
"""        
            
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        di={}
        flag=0
        flagg=0
        for i in range(n):
            di[a[i]]=0
        for i in range(n):
            if a[i]>b[i]:
                flag+=1
            if a[i]==b[i]:
                flagg+=1
            di[a[i]]+=1        
            if b[i] in di:
                di[b[i]]+=1
            
        pos=0
        if flag==0 or flag==1:
            for i in di:
                if di[i]<2 and pos!=0:
                    flag=2
                    break
                pos+=1
        if flag>1 or flagg>1:
            print("NO")
        else:
            print("YES")
                
"""       
                


"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a1=sum(a)
        a2=sum(b)
        if a!=b and a2%a1==0:
            print("YES")
        else:
            print("NO")
"""
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        flag=0
        for i in range(1,n):
            if a[i]>b[i]:
                flag=1
                print("NO")
                break
        if flag==0:
            print("YES")
"""
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a1=set(a)
        a2=set(b)
        if (len(a1|a2)==n or sum(a1)<sum(a2)) and len(a1)!=len(a) and len(a2)!=len(b):
            print("YES")
        else:
            print("NO")
"""
"""
t,s=map(int,input().split())
if s==1:
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        sa=set(a)
        sb=set(b)
        a1=sum(a)
        a2=sum(b)
        if a1<a2 and len(sa|sb)<=n:
            print("YES")
        else:
            print("NO")
"""
