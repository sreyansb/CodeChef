for i in range(int(input())):
    r,c,q=map(int,input().split())
    li=[[0 for i in range (c)] for j in range (r)]
    rdi={}
    cdi={}
    count=0
    for i in range(q):
        a,b=map(int,input().split())
        a,b=a-1,b-1
        if a not in rdi:
            rdi[a]=0
        rdi[a]^=1
        if b not in cdi:
            cdi[b]=0
        cdi[b]^=1
    for i in rdi:
        if rdi[i]:
            for j in range(c):
                li[i][j]^=1
    for i in cdi:
        if cdi[i]:
            for j in range(r):
                li[j][i]^=1
    for i in range(r):
        count+=sum(li[i])
    print(count)
        
    """l=[[0]*c]*r
    r1=[]
    c1=[]
    count=0
    for i in range(q):
        a,b=map(int,input().split())
        r1.append(a-1)
        c1.append(b-1)
    r2=set(r1)
    c2=set(c1)
    for i in r2:
        j=r1.count(i)%2
        if j:
            for k in range (c):
                l[i][k]^=1
                if l[i][k]:
                    count+=1
                else:
                    count-=1
    
    for i in c2:
        j=c1.count(i)%2
        if j:
            for k in range (r):
                l[k][i]^=1
                if l[k][i]:
                    count+=1
                else:
                    count-=1
    print(count)"""
                
    """li=[[0]*c]*r
    for i in range(q):
        a,b=map(int,input().split())
        a,b=a-1,b-1
        for z in range(c):
            li[a][z]^=1
        for y in range(r):
            li[y][b]^=1"""
        
    
    """
    
    for j in range(q):
        a,b=map(int,input().split())
        a,b=a-1,b-1
        for k in range(m):
            li[a][k]+=1
            if li[a][k]%2==1:
                count+=1
            else:
                count-=1
        for h in range(n):
            li[h][b]+=1
            if li[h][b]%2==1:
                count+=1
            else:
                count-=1
    print(count)
    """
